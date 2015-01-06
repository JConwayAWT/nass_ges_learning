Traffic Accident Analysis (Extension) Using Machine Learning

The goal of this project is to accurately predict the severity of a traffic accident given the preceding conditions.  If we can do a good job of predicting the outcome of being in some circumstance, that essentially means that we also know what situations we should avoid putting ourselves into.  As automated vehicles begin to move out of their infancy in 2014/2015, we should be preparing ourselves to handle the complexity that comes along with machines solving such complicated problems.  Inevitably, mistakes will be made, whether by humans, machines, or both.  The goal of this project is to ensure that we have a method through which we can systematically learn from those mistakes.  In particular, of course, the machines will be learning.

To get started on this, I've taken the most recent accident information available from the NASS GES traffic data sets, collected in the United States.  The general method is that we take the data, split it into different categories based on accident severity, split each category into training and testing data, and then try a number of different classifiers on each set.  Of course, each classifier will be subject to a wide variety of parameter combinations along the way.

To get started, you can follow these steps:

* Make sure that you have Python installed.  I used 2.7.5, but most of the code is 2-3 ambiguous (print statements!).
* Make sure that you have Scikit Learn installed.  I used v0.14.1.
* Clone the repository into whatever directory you'd like.
* Begin by executing "head_on_extraction.py", which splits the data into the relevant training/testing sets.
* Now, you can run any of the remaining scripts.  The console will update you on what's being tested and the accuracy of that model.

Of course, there's still a ton of work to be done.  I'm not a machine learning expert, and even so, this was only a side project.  However, the results do seem promising so far.  For more details on what else could be done from here and my results so far, check out the PDF document in the repo.

Have fun!