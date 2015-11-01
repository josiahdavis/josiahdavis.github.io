---
layout: default
title: How to Perform Natural Language Processing in R
---
When I started learning NLP in R I found resources here and there but I never found a great resource for learning the syntax. This is the reference guide I wish I had when I started learning NLP. You can find the data I'm using in these examples [here](https://github.com/josiahdavis/nlp-in-R).

<div style="overflow:auto;"><div class="geshifilter"><pre class="r geshifilter-R" style="font-family:monospace;"><span style="color: #666666; font-style: italic;"># ANALYSIS OF YELP DATA</span>
<span style="color: #666666; font-style: italic;"># This script performs a number of NLP techniques including:</span>
<span style="color: #666666; font-style: italic;">#   - Tagging Parts of Speech</span>
<span style="color: #666666; font-style: italic;">#   - Filtering for only Nouns and Adjectives</span>
<span style="color: #666666; font-style: italic;">#   - Removing Stopwords</span>
<span style="color: #666666; font-style: italic;">#   - Stemming Words</span>
<span style="color: #666666; font-style: italic;">#   - Applying a custom tokenizer</span>
<span style="color: #666666; font-style: italic;">#   - Identifying the most frequent words</span>
<span style="color: #666666; font-style: italic;">#   - Calculating the most interesting word</span>
<span style="color: #666666; font-style: italic;">#   - Count the number of positive and negative sentiments</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Read in the data</span>
loc <span style="">&lt;-</span> <span style="color: #0000ff;">'/Users/josiahdavis/Documents/GitHub/earl/data/'</span>
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a> <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/utils/read.csv"><span style="color: #003399; font-weight: bold;">read.csv</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/paste"><span style="color: #003399; font-weight: bold;">paste</span></a><span style="color: #009900;">&#40;</span>loc<span style="color: #339933;">,</span> <span style="color: #0000ff;">'yelp_reviews.csv'</span><span style="color: #339933;">,</span> sep=<span style="color: #0000ff;">&quot;&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># ========================== # </span>
<span style="color: #666666; font-style: italic;"># ---- PARTS OF SPEECH ----</span>
<span style="color: #666666; font-style: italic;"># ========================== #</span>
&nbsp;
<a href="http://inside-r.org/r-doc/base/library"><span style="color: #003399; font-weight: bold;">library</span></a><span style="color: #009900;">&#40;</span>magrittr<span style="color: #009900;">&#41;</span>
<a href="http://inside-r.org/r-doc/base/library"><span style="color: #003399; font-weight: bold;">library</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/packages/cran/openNLP"><span style="">openNLP</span></a><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Convert text to string format </span>
texts <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/lapply"><span style="color: #003399; font-weight: bold;">lapply</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>text<span style="color: #339933;">,</span> as.String<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Define types of annotations to perform</span>
tagging_pipeline <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/list"><span style="color: #003399; font-weight: bold;">list</span></a><span style="color: #009900;">&#40;</span>
  Maxent_Sent_Token_Annotator<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span>
  Maxent_Word_Token_Annotator<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span>
  Maxent_POS_Tag_Annotator<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Define function for performing the annotations</span>
annotate_entities <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>doc<span style="color: #339933;">,</span> annotation_pipeline<span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
  annotations <span style="">&lt;-</span> annotate<span style="color: #009900;">&#40;</span>doc<span style="color: #339933;">,</span> annotation_pipeline<span style="color: #009900;">&#41;</span>
  AnnotatedPlainTextDocument<span style="color: #009900;">&#40;</span>doc<span style="color: #339933;">,</span> annotations<span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Annotate the texts</span>
texts_annotated <span style="">&lt;-</span> texts %<span style="">&gt;</span>% <a href="http://inside-r.org/r-doc/base/lapply"><span style="color: #003399; font-weight: bold;">lapply</span></a><span style="color: #009900;">&#40;</span>annotate_entities<span style="color: #339933;">,</span> tagging_pipeline<span style="color: #009900;">&#41;</span>
<a href="http://inside-r.org/r-doc/utils/str"><span style="color: #003399; font-weight: bold;">str</span></a><span style="color: #009900;">&#40;</span>texts_annotated<span style="color: #009900;">&#91;</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">,</span> max.level = <span style="color: #cc66cc;">2</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Define the POS getter function</span>
POSGetter <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>doc<span style="color: #339933;">,</span> parts<span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
  <a href="http://inside-r.org/r-doc/mgcv/s"><span style="color: #003399; font-weight: bold;">s</span></a> <span style="">&lt;-</span> doc<span style="">$</span>content
  a <span style="">&lt;-</span> annotations<span style="color: #009900;">&#40;</span>doc<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#91;</span><span style="color: #009900;">&#91;</span><span style="color: #cc66cc;">1</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#93;</span>
  k <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/sapply"><span style="color: #003399; font-weight: bold;">sapply</span></a><span style="color: #009900;">&#40;</span>a<span style="">$</span>features<span style="color: #339933;">,</span> <span style="color: #0000ff;">`[[`</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">&quot;POS&quot;</span><span style="color: #009900;">&#41;</span>
  <span style="color: #000000; font-weight: bold;">if</span><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/sum"><span style="color: #003399; font-weight: bold;">sum</span></a><span style="color: #009900;">&#40;</span>k <span style="">%in%</span> parts<span style="color: #009900;">&#41;</span> <span style="">==</span> <span style="color: #cc66cc;">0</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#123;</span>
    <span style="color: #0000ff;">&quot;&quot;</span>
  <span style="color: #009900;">&#125;</span><span style="color: #000000; font-weight: bold;">else</span><span style="color: #009900;">&#123;</span>
    <a href="http://inside-r.org/r-doc/mgcv/s"><span style="color: #003399; font-weight: bold;">s</span></a><span style="color: #009900;">&#91;</span>a<span style="color: #009900;">&#91;</span>k <span style="">%in%</span> parts<span style="color: #009900;">&#93;</span><span style="color: #009900;">&#93;</span>
  <span style="color: #009900;">&#125;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Identify the nouns</span>
nouns <span style="">&lt;-</span> texts_annotated %<span style="">&gt;</span>% <a href="http://inside-r.org/r-doc/base/lapply"><span style="color: #003399; font-weight: bold;">lapply</span></a><span style="color: #009900;">&#40;</span>POSGetter<span style="color: #339933;">,</span> parts = <a href="http://inside-r.org/r-doc/base/c"><span style="color: #003399; font-weight: bold;">c</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">&quot;JJ&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;JJR&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;JJS&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;NN&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;NNS&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;NNP&quot;</span><span style="color: #339933;">,</span>
                                                         <span style="color: #0000ff;">&quot;NNPS&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
<span style="color: #666666; font-style: italic;"># Full list: https://goo.gl/OXLNIF</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Turn each character vector into a single string</span>
nouns <span style="">&lt;-</span> nouns %<span style="">&gt;</span>% <a href="http://inside-r.org/r-doc/base/lapply"><span style="color: #003399; font-weight: bold;">lapply</span></a><span style="color: #009900;">&#40;</span>as.String<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># ============================= # </span>
<span style="color: #666666; font-style: italic;"># ---- TEXT TRANSFORMATION ----</span>
<span style="color: #666666; font-style: italic;"># ============================= #</span>
&nbsp;
<a href="http://inside-r.org/r-doc/base/library"><span style="color: #003399; font-weight: bold;">library</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/packages/cran/tm"><span style="">tm</span></a><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Convert to dataframe</span>
d <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/data.frame"><span style="color: #003399; font-weight: bold;">data.frame</span></a><span style="color: #009900;">&#40;</span>reviews = <a href="http://inside-r.org/r-doc/base/as.character"><span style="color: #003399; font-weight: bold;">as.character</span></a><span style="color: #009900;">&#40;</span>nouns<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Replace new line characters with spaces</span>
d<span style="">$</span>reviews <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/gsub"><span style="color: #003399; font-weight: bold;">gsub</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">&quot;<span style="color: #000099; font-weight: bold;">\n</span>&quot;</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">&quot; &quot;</span><span style="color: #339933;">,</span> d<span style="">$</span>reviews<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Convert the relevant data into a corpus object with the tm package</span>
d <span style="">&lt;-</span> Corpus<span style="color: #009900;">&#40;</span>VectorSource<span style="color: #009900;">&#40;</span>d<span style="">$</span>reviews<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Convert everything to lower case</span>
d <span style="">&lt;-</span> tm_map<span style="color: #009900;">&#40;</span>d<span style="color: #339933;">,</span> content_transformer<span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/tolower"><span style="color: #003399; font-weight: bold;">tolower</span></a><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Stem words</span>
d <span style="">&lt;-</span> tm_map<span style="color: #009900;">&#40;</span>d<span style="color: #339933;">,</span> stemDocument<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Strip whitespace</span>
d <span style="">&lt;-</span> tm_map<span style="color: #009900;">&#40;</span>d<span style="color: #339933;">,</span> stripWhitespace<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Remove punctuation</span>
d <span style="">&lt;-</span> tm_map<span style="color: #009900;">&#40;</span>d<span style="color: #339933;">,</span> removePunctuation<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># ============================== # </span>
<span style="color: #666666; font-style: italic;"># ---- DOCUMENT TERM MATRIX ----</span>
<span style="color: #666666; font-style: italic;"># ============================== #</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Create a frequency-based document term matrix of unigrams</span>
dtm1 <span style="">&lt;-</span> DocumentTermMatrix<span style="color: #009900;">&#40;</span>d<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Define a custom tokenizer</span>
BigramTokenizer <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
  <a href="http://inside-r.org/r-doc/base/unlist"><span style="color: #003399; font-weight: bold;">unlist</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/lapply"><span style="color: #003399; font-weight: bold;">lapply</span></a><span style="color: #009900;">&#40;</span>ngrams<span style="color: #009900;">&#40;</span>words<span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span> <a href="http://inside-r.org/r-doc/base/c"><span style="color: #003399; font-weight: bold;">c</span></a><span style="color: #009900;">&#40;</span><span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span> <span style="color: #cc66cc;">2</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span> <a href="http://inside-r.org/r-doc/base/paste"><span style="color: #003399; font-weight: bold;">paste</span></a><span style="color: #339933;">,</span> <a href="http://inside-r.org/r-doc/nlme/collapse"><span style="color: #003399; font-weight: bold;">collapse</span></a> = <span style="color: #0000ff;">&quot; &quot;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span>
         use.names = <span style="color: #000000; font-weight: bold;">FALSE</span><span style="color: #009900;">&#41;</span>  
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Create a tf-idf weighted document term matrix with a custom tokenizer</span>
dtm2 <span style="">&lt;-</span> DocumentTermMatrix<span style="color: #009900;">&#40;</span>d<span style="color: #339933;">,</span> <a href="http://inside-r.org/r-doc/boot/control"><span style="color: #003399; font-weight: bold;">control</span></a> = <a href="http://inside-r.org/r-doc/base/list"><span style="color: #003399; font-weight: bold;">list</span></a><span style="color: #009900;">&#40;</span>weighting = weightTfIdf<span style="color: #339933;">,</span>
                                            tokenize = BigramTokenizer<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Convert from sparse to dense matrix</span>
dtm2 <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/as.matrix"><span style="color: #003399; font-weight: bold;">as.matrix</span></a><span style="color: #009900;">&#40;</span>dtm2<span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Identify the most interesting word for each review</span>
words <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/colnames"><span style="color: #003399; font-weight: bold;">colnames</span></a><span style="color: #009900;">&#40;</span>dtm2<span style="color: #009900;">&#41;</span>
getInterestingWord <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#123;</span>
  words<span style="color: #009900;">&#91;</span><a href="http://inside-r.org/r-doc/base/which.max"><span style="color: #003399; font-weight: bold;">which.max</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#93;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Apply the previously created function to each review</span>
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>word <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/apply"><span style="color: #003399; font-weight: bold;">apply</span></a><span style="color: #009900;">&#40;</span>dtm2<span style="color: #339933;">,</span> MARGIN = <span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span> FUN = <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span> getInterestingWord<span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Calculate words length</span>
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>length <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/apply"><span style="color: #003399; font-weight: bold;">apply</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/as.matrix"><span style="color: #003399; font-weight: bold;">as.matrix</span></a><span style="color: #009900;">&#40;</span>dtm1<span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span> MARGIN = <span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span> FUN = <a href="http://inside-r.org/r-doc/base/sum"><span style="color: #003399; font-weight: bold;">sum</span></a><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># ============================== # </span>
<span style="color: #666666; font-style: italic;"># ---- SENTIMENT ANALYSIS ----</span>
<span style="color: #666666; font-style: italic;"># ============================== #</span>
&nbsp;
<a href="http://inside-r.org/r-doc/base/library"><span style="color: #003399; font-weight: bold;">library</span></a><span style="color: #009900;">&#40;</span>syuzhet<span style="color: #009900;">&#41;</span>
<a href="http://inside-r.org/r-doc/base/library"><span style="color: #003399; font-weight: bold;">library</span></a><span style="color: #009900;">&#40;</span><a href="http://inside-r.org/packages/cran/plyr"><span style="">plyr</span></a><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># For each review, calculate the count of negative and positive sentiments</span>
getSentiment <span style="">&lt;-</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#123;</span>
  <a href="http://inside-r.org/r-doc/base/colSums"><span style="color: #003399; font-weight: bold;">colSums</span></a><span style="color: #009900;">&#40;</span>get_nrc_sentiment<span style="color: #009900;">&#40;</span>get_sentences<span style="color: #009900;">&#40;</span><a href="http://inside-r.org/r-doc/base/as.character"><span style="color: #003399; font-weight: bold;">as.character</span></a><span style="color: #009900;">&#40;</span>x<span style="">$</span>text<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#91;</span><a href="http://inside-r.org/r-doc/base/c"><span style="color: #003399; font-weight: bold;">c</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">&quot;negative&quot;</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">&quot;positive&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Apply function to each row of the dataframe</span>
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a> <span style="">&lt;-</span> adply<span style="color: #009900;">&#40;</span><a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="color: #339933;">,</span> <span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span> <a href="http://inside-r.org/r-doc/base/function"><span style="color: #003399; font-weight: bold;">function</span></a><span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span> getSentiment<span style="color: #009900;">&#40;</span>x<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span>
&nbsp;
<span style="color: #666666; font-style: italic;"># Create two helper variables</span>
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>positivity <span style="">&lt;-</span> <a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>positive <span style="">/</span> <a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>wordsLength
<a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>negativity <span style="">&lt;-</span> <a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>negative <span style="">/</span> <a href="http://inside-r.org/packages/cran/dr"><span style="">dr</span></a><span style="">$</span>wordsLength</pre></div></div>
