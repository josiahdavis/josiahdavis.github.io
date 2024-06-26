---
layout: post
title:  "Training Compute Optimal Models"
date:   2024-05-29 10:06:33 -0500
---

>Some notes on Chinchilla (https://arxiv.org/pdf/2203.15556.pdf) and how we might apply it more broadly to our own deep learning projects:

### Contents

1. **Overview:** What does “Training compute-optimal models” mean?
2. **Application #1:** Given a compute budget, how large of a model and how much data should we be aiming for?
3. **Application #2:** Given a limited dataset size, how large of a model should we train?
4. **Reproducibility:** Code to derive the linear models for predicting optimal values.

### Overview: What does “Training compute-optimal models” mean?

This paper (“Chinchilla”) demonstrates how to pick the *optimal* model size and training data required for a given compute budget. Optimality is defined as get the most “bang for buck”: maximizing model accuracy for the given compute budget. 

The authors use three different quantitative approaches, to answer this question. Approach #2 is highlighted here (although all three approaches arrive at similar conclusions).

They train dozens of different sized models and dataset sizes, varying them across 9 different compute budgets (left image below). Then they fit a parabola on the loss and identify the minimum for the optimal number of parameters and tokens for each compute budget. Finally, they demonstrate that a linear relationship exists between compute and optimal parameter count (center image) and data size (right image).

![Image](/assets/chinchilla_image_1.jpg)

<center><b>Figure 1:</b> Identifying a linear relationship between compute budget and parameter count and data size.Image source is Chinchilla paper https://arxiv.org/pdf/2203.15556.pdf.</center>
<br>

The big application from their paper is that a lot of the newest models at the time were much larger than they needed to be, given their training data size, and the authors proved this by training a much smaller model (“Chinchilla”) that was just as good as the larger models. 

Now, let’s discuss now two ways in which we can apply this paper to our own deep learning projects.

### Application #1: Given a compute budget, how large of a model and how much data should we be aiming for?

As an example, let’s say that you have a compute budget of a single p4 instance (8xA100), and you can train for up to one day with it. 

That corresponds to a compute budget of 1.08e20 FLOP.

In order to achieve the lowest possible loss *with that compute budget*, you should train a model with $$N \propto 900M$$ parameters and $$D\propto19B$$ tokens of data. 

See table below for more examples:

|Description	|Training Time (days)	|GPUs (#)	|Peak FLOP/s	|Utilization rate	|Compute Budget (FLOP)	|Parameters (M)	|Data (B)	|
|---	|---	|---	|---	|---	|---	|---	|---	|
|1xV100, 6 hours	|0.25	|1	|1.57E+13	|0.5	|1.70E+17	|40	|0.71	|
|8xV100, 1 day	|1	|8	|1.57E+13	|0.5	|5.43E+18	|219	|4	|
|8xA100, 1 day	|1	|8	|3.12E+14	|0.5	|1.08E+20	|946	|19	|
|16xH100, 2 weeks	|14	|16	|1.98E+15	|0.4	|1.53E+22	|10,727	|238	|
|400xH100, 4 weeks	|28	|400	|1.98E+15	|0.4	|7.66E+23	|72,926	|1,751	|

Here are some details about this table:

* **Peak FLOP/s**: From NVIDIA's fact sheets: [H100](https://resources.nvidia.com/en-us-tensor-core/nvidia-tensor-core-gpu-datasheet), [A100](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf), [V100](https://images.nvidia.com/content/technologies/volta/pdf/volta-v100-datasheet-update-us-1165301-r5.pdf). I use values for BF16 on Tensor Cores for A100, H100.
* **Utilization rate**:  FLOP achieved  / FLOP promised by NVIDIA. For FLOP achieved, I’m using a placeholder value based off what I’ve seen using PyTorch, BF16 on 8xA100.
* **Compute Budget**: Training time x GPUs x Peak FLOP/s x Utilization rate
* **Parameters (M)** I fit a linear model on data from Table A3 of the Chinchilla paper (Approach 2) yeilding:

$$log_{10}​(N)=0.48994161286254695 ∗ log_{10}​(C)-0.8390004003190913 $$

* **Data (B)**  I fit a linear model on data from Table A3 of the Chinchilla paper (Approach 2) yeilding: 

$$log_{10}​(D) = 0.5100202250950424 * log_{10}​(C) + 0.061740265574555316 $$

As a convenience, here is a function you can use to predict the optimal data/model size from the compute budget:

{% highlight python %}

import numpy as np

def predict_model_from_compute(compute):
    return 10 ** (0.48994161286254695 * np.log10(compute) - 0.8390004003190913)

def predict_data_from_compute(compute):
    return 10 ** (0.5100202250950424 * np.log10(compute) + 0.061740265574555316)

{% endhighlight %}

### Application #2: Given a limited dataset size, how large of a model should we train?

If your dataset is relatively small, then you are not really in a compute-bound situation, where you need to worry about training compute budget per-se. 

How small is small? We could somewhat arbitrarily choose a value e.g., $$D<4B$$ (corresponding to a single 8xV100 node from the table above), although this threshold will vary based off of what compute resources you happen to have.

Regardless of the specific threshold, if you find yourself in a data-constrained regime, the question should be modified: given the amount of training data I actually have, how large of a model should I train?

Again, we can take data Table A3 (using Approach 2) and fit a linear model, but this time mapping between data and model size, yielding: 

$$log_{10}​(N)=0.9606135203483422∗log_{10}​(D)−0.8980869297587599 $$

<center><img src="/assets/compute_optimal_2.jpg"></center>
<center><b>Figure 2:</b> Predicting the Optimal Model size from the amount of training data. Data source is the Chinchilla paper https://arxiv.org/pdf/2203.15556.pdf.</center>
<br>

Here are some example values of predicting the optimal model size:

|Data Size (Given)	| Model Size (Predicted)	|
|---	|---	|
|1E06	|7.34E07	|
|1E09	|5.59E07	|
|1E10	|5.11E08	|
|1E11	|4.66E09	|
|1E12	|4.26E10	|
|1E14	|3.55E12	|


As a convenience, here is a python function to compute the optimal model size given the data size:

{% highlight python %}

import numpy as np

def predict_model_from_data(data):
    return 10 ** (0.9606135203483419 * np.log10(data) - 0.8980869297587544)

{% endhighlight %}

### Reproducibility: Code to derive the linear models for predicting optimal values.

Here is how you can reproduce the linear interpolations to predict optimal model size from the given data size (and plot it).

I will demonstrate this for the case of predicting the model size from the data, but the data is also below to do the same thing for the model and data size from the compute.

As an arbitrary example, let's say you have an existing 1B model trained on 10^11 tokens so we have a reference point to add to our plot.

{% highlight python %}
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Import data from Table A3 (approach 2)
d = pd.DataFrame(
    [
        [400e6, 7.7e9, 1.84e19],
        [1e9, 20.0e9, 1.20e20],
        [10e9, 219.5e9, 1.32e22],
        [67e9, 1.7e12, 6.88e23],
        [175e9, 4.3e12, 4.54e24],
        [280e9, 7.1e12, 1.18e25],
        [520e9, 13.4e12, 4.19e25],
        [1e12, 26.5e12, 1.59e26],
        [10e12, 292.0e12, 1.75e28],
    ],
    columns=["Params", "Tokens", "Compute"],
)

# 2. Fit line
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html

x = np.log10(d["Tokens"].values)
y = np.log10(d["Params"].values)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0] 
print(f"Params = {m} x Data + {c}")
# > Params = 0.9606135203483419 x Data + -0.8980869297587544

def predict(d):
    return 10**(m * np.log10(d) + c)

# 3. Create a nice plot
x_for_line = np.linspace(start=d["Tokens"].min(), stop=d["Tokens"].max())
plt.figure(figsize=(5, 5))
plt.scatter(d["Tokens"], d["Params"], label="Chinchilla data (Approach 2)", zorder=3, color="k")
plt.plot(x_for_line, predict(x_for_line), color="tab:orange", label="Fitted Line", zorder=2)
plt.scatter([1e11], [10**9], color="tab:blue", marker="*", s=150, label="Current model", zorder=3)
plt.scatter([1e11], [predict([1e11])], color="tab:green", marker="*", s=150, label="Optimal model (predicted)", zorder=3)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Data (D)")
plt.ylabel("Parameters (N)")
plt.title("Compute Optimal Models")
plt.legend()
plt.grid()
plt.show()

{% endhighlight %}

***

### Appendix – Table A3 Sanity Check

Here is a quick sanity check I did to make sure that my linear models were correct. As you can see from the last two columns, it's not exaclty the same, but it's pretty close.

|	|My Predictions	| | What was Reported | 	|Ratio	|
|---	|---	|---	|---	|
|Compute	|Parameters (B)	|Data (B)	|Parameters (B)	|Data (B)	|Parameters (B)	|Data (B)	|
|1.84E+19	|0.40	|7.71	|0.40	|7.70	|0.99	|1.00	|
|1.20E+20	|1.00	|20.07	|1.00	|20.00	|1.00	|1.00	|
|1.32E+22	|9.97	|220.64	|10.00	|219.50	|1.00	|0.99	|
|6.88E+23	|69.19	|1,657.27	|67.00	|1,700.00	|1.03	|1.03	|
|4.54E+24	|174.39	|4,338.48	|175.00	|4,300.00	|1.00	|0.99	|
|1.18E+25	|278.46	|7,061.67	|280.00	|7,100.00	|0.99	|1.01	|
|4.19E+25	|518.07	|13,476.83	|520.00	|13,400.00	|1.00	|0.99	|
|1.59E+26	|995.76	|26,606.19	|1,000.00	|26,500.00	|1.00	|1.00	|
|1.75E+28	|9,964.13	|292,590.95	|10,000.00	|292,000.00	|1.00	|1.00	|