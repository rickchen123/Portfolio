# An analysis of the Twitter of politicians
---------------------------------------
# Purpose

The purpose of the repository is analyzing the Twitter use of Donald Trump and Barack Obama. First, we briefly plot the usage of the twitter for both presidents,e.g frequency of tweets, popularity change, etc. Then we did the text processing with NLTK to explore aggregate text statistics of the speeches and visualize some of their properties.Exploring some of the relations between the properties of the tweets, time, provide a novel visualization of the relevant information. Next, we analyzed the topic change between the president's Obama last 10 Months and president's Trump first 10 twitter. We used the word cloud for most frequent word, and LDA for the analysis of the topic change. Lastly, the Presidential Job Approval Rating from UCSB as a response variable to find whether the Approval Rating can be predicted by the twitter data.

# Introduction

The purpose of the repository is analyzing the Twitter use of Donald Trump and Barack Obama. We would like to use our knowledge, learn in stat 159, to summarize what they wrote in Twitter in order to find the differnce between Mr. Trump and Mr. Obama. We think the public tweets posted by them may indicates their personal characters, purposes and principles.

- In Notebook 1, we use the raw data with datetime to plot histogram and series graph.

- In Notebook 2, we did some text processing with NLTK to compute aggregate text statistics of the speeches as well as visualize some of their properties. Explore some of the relations between the properties of the tweets, time, provide a novel visualization of the relevant information.

- In Notebook 3(Analysis Notebook), we analyze the topic change between the president's Obama last 10 Months and president's Trump first 10 twitter. First we will use the word cloud to show the most frequent stemmed words of Trump and Obama's Twitter. Then we will use the LDA to analyze the topic of the president's Obama last 10 Months and president's Trump first 10 twitter.

- In Notebook 4(Analysis Notebook), we will use the Presidential Job Approval Rating from UCSB as a response variable to evaluate our model. And then we do a sentiment anaylsis of Trump and Obama twitter data by using the Sentiment Anaylzer from the NLTK package Then, we will test it with R-squared to see the correlation between the predictors variables and response variable. Lastly, we will use the OLS regresion to find out whether the Approval Rating can be predicted.

# Installation
Clone the repository and run the following commands in your terminal.
```
make clean
make env
source activate twitter
make test
make run
```
# Package Requirement
The wordlcoud and pyLDAvis needed to be install using `pip` install
```
pip install wordcloud
pip install pyLDAvis
```
# LICENSE CONDITIONS for this dataset 

Copyright (c) 2014 ESPN Internet Ventures

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
