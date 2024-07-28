# Arttificial Intelligence

    - The ability to make a decision based on preexisted knowledge.
    - Enabling computer program to make decisions in a way that mimic human mental capabilities.

# AI applications

    - Loan decisions
    - Diagnose Patiems
    - Autocompleting texts
    - Face Detection

# How to apply AI:

    - Classic AI and Machine Learning.
    - Classic AI: symbolic learning in which human knowledge is represented by symbols and relations.
        - Knowledge-base |-> Inference Engine |-> Results
    - Machine Learning: provides systems the ability to automatically learn to make decisions from experience without being explicitly programmed.
        - Types of Learning: Supervised and Unsupervised Learning.
            - Suervised Learning uses numeric values.
            - Unsupervised Learning uses categorical values.

## Machine Learning

    -  Learning:
        - Supervised: 
            - Classification:
                - Binary Classification
                - Multi Classification
            - Regression
                - Linear Regression
                - Non-linear Regression
        - Unsupervised
            - Clustering
            - Anomaly Detection
            - Dimensionality Reduction
            - Association Rule Learning

## Supervised Learning

    - most used
    - uses labeled data/features
    - classifies or predicts target variables
    - Features: input data that the model uses to make predictions.
    - Labels: outcomes or categories that the model predicts or classifies based on the input data.
    - Datasets:
        - Training Datesets: subset of data used to train the model and learn patterns.
        - Testing Datasets: subset of data used to evaluate the model's performance and its ability to generalise.
    - Learning Model: algorithm or system that uses input data (features) and corresponding target values (labels) to learn patterns and make predictions or classifications.

## Unsupervised Learning

    - Uses unlabeled data or predefined categories
    - Learns through observation & find structures in data
    - Clustering: Grouping similar data points into clusters based on their features.
    - Anomaly Detection: Identifying unusual or outlier data points that deviate from the norm.
    - Dimensionality Reduction: Reducing the number of features while preserving important information.
    - Association Rule Learning: Finding relationships or associations between variables in the data.

### Regression

    1. What is a Regression?
    2. Linear Regression
    3. Gradient Descent
    4. Polynomial Functions
    5. Non-liner Regression
    6. Linear Algebra
    7. Normal Equations

### What is Regression

    - A statistical approach for modelling the relationship between variable x (features) and value y (target).
    - Model: relationship or function that maps input features to continuous target values.
    - Models enables the prediction of numerical outcomes based on learned patterns from the data.
        - Example: f(x) = 2x
    - Linear and Linear Regression:
        - Linear: first-degree equations
        - Non-linear: higher than one degree or complex.
    - Best fitting line: straight line that most closely matches the data points by minimising the overall prediction errors.
    - Linear function - the general form:
        - f(x) = \theta*x + b
            - f(x)    ... model |-> y (model output)
            - x       ... input feature (independent variable)
            - \theta: ... coefficient (slope of the line))
            - b       ... Y-intercept (bias)
        - \theta (Slope): determines the angle or steepness of the line:
            - positive \theta indicates an upward slope.
            - negative \theta indicates a downward slope.
        - b (Y-Intercept): moves the line up or down. 
            - positive b shifts the line upward.
            - negative b shifts the line downward.
        - \theta and b (summary): \theta defines slope and defines vertical poistion.
        - Example: f(x) = x
            - represents a linear model where:
                - the coefficient, \theta or slope, is 1, and the Y-intercept is 0.
                - f(x) = 1x + 0 = x
    - In summary, 

## Linear Regression

    - Machine Learning is centered on that \theta controls the angle or steepness of the line, and b adjusts its position.
    - Example: model -> f(x) = 2x + 1
        x   y
        -1  -1  
        0   1
        1   3
        2   5
        3   7
        4   9
    - Using the given model f(x) = 2x + 1, and x values, we are able to compute y values.
    - In ML, the model is not given, and our task is to find a model for a given data.
    - Example:  Find a model for the following dataset.
        f(x) = ???
        Features ->  x   -1  0   1   2   3   4   5 <- Unseen
        Labels   ->  y   -1  1   3   5   7   9   ? <- Target
    Steps:
        1. Visualise
        2. Find parameter \theta
        3. Fimd Parameter b

        1. Visualise:
            10 +------------------------------------------------------------------+
                |       +        +       +        +       +***    +        +       |
                |                                       ***  f(x) = 2x + 1 ******* |
            8   |-+                                  ***                         +-|
                |                                  ***                             |
                |                               ***                                |
            6   |-+                          ***                                 +-|
                |                         ***                                      |
                |                       ***                                        |
        y   4   |-+                  ***                                         +-|
                |                 ***                                              |
                |               ***                                                |
            2   |-+          ***                                                 +-|
                |         ***                                                      |
                |      ***                                                         |
            0   |-+  ***                                                         +-|
                | ***   +        +       +        +       +       +        +       |
                +------------------------------------------------------------------+
            -1       0        1       2        3       4       5        6       7

            gnuplot> set title "Plot of f(x) = 2x + 1"
            gnuplot> set xlabel "x"
            gnuplot> set ylabel "f(x)"
            gnuplot> set xrange [-10:10]   # Set x-axis range from -10 to 10
            gnuplot> set yrange [-20:20]   # Set y-axis range from -20 to 20
            gnuplot> plot 2*x + 1 title "f(x) = 2x + 1"

        2. Find parameter \theta or slope:
            - select any two points from the dataset. For example, (3, 7) and (4, 9)
    
            \theta  = (y2 - y1)/(x2 - x1)
                    = (9 - 7)/(4 - 3) = 2
            \theta  = 2

            - from calcules, we know that slope is the first derivative of a linear function.
                \theta = f(x)'
                f(x)' = 2
            - However, we still need to find f(x) not its derivative.
            - Also, we know that the derivative of a function can be reverted to its original form by integrating it.
                ∫f(x)' = 2x + b
            - now we need to find value of paramter b to complete the integration.
        
        3. Find Parameter b:
            - Y-intercept or vertical positioning.
            - to find constant b of a linear function
                b = y̅ - \theta*x̅
                b = average_y - \theta*average_\theta
                b = (24/6) - 2(9/6) = 1

            - now the model is f(x) = 2x + 1
            - now we can predict future x values, for example, find value of 5.
                2x + 1 = 2*5 + 1 = 11
    - For now we only have one feature and coefficient, \theta and x, but in reality we have more than 2D.
        - f(x) = \theta_0 + \theta_1*x_1
    - Therefore, from now on, we deal with our linear equation using the following form 
        h(x) = \theta_i*x_i + b
        - h ... means hypothesis
        - i ... indicates that we have more than one feature.
    - Structure of supervised learning:
        Training datasets |-> Learning Aalgorithm |-> Model 
    - Add new feature z:
        - nw we have three axes: x,y, and z - two features (x, z) and one label (y).
        - h(x) = \theta_0 + \theta_1*x_1 + \theta_2*x_2
            - find \theta_0, \theta_1, \theta_2
    - Add n features:
        h(x) = \theta_0*x_1 + \theta_1*x_1, \theta_2*x_2, ..., \theta_j*x_j where x_0   = 1
        - we can simplify this term to:
            h(x) = {\sum}_{j=0}^{n=0}{\theta_j*x_j}                         where n     = number of features
                                                                                  j     = counter
        - alse, we can represent \theta and x with single coulm matrix.
    - The job of the learning algorithm is to find \theta_n values sych that h(x) ≃ y.

### Cost Function

    - Example: Find \theta_n
        Size    Rooms   Price
        100     4       6000

        y = \theta_0 + \theta_1*100 + \theta_2*4
    - the learning  algorithms is starts with initial solution and enhance with each iteration.
        \theta_n (\theta_0 = 50, \theta_1 = 50, \theta_2 = 100)
        y = 50 + 50*100 + 100*4 = 5450
    - the predicted value of y is 5450, but the real value is 6000 with ddifference of 550.
    - this difference is called error.
    - change \theta values to minimise the error/cost/loss.
    - calculate the sqaued differen cebetween the actual value h(x) and the predicted value
        (h(x) - y)^2
        (6000 - 5450)^2 = 302500 <- represents Cost/Loss function.
    - our objective is to choose values of \theta to minimise the cost/loss/error
    - simplify:
        min(h(x) - y)^2
        h(x) = min \sum_{i=1}^{m}(h(x_i) - y_i)^2
    - this cost function is known but Ordinary Least Squares as defined as follows:
        j(\theta) = 1/2 \sum_{i=1}^{m}(h(x_i) - y_i)^2
    - the goal of learning is to minimise the cost function j(\tehta).

## Gradient Descent

    - The goal of learning is to minimise the cost function j(\theta).
        j(\theta) = 1/2 \sum_{i=1}^{m}(h(x_i) - y_i)^2

    - we see that j(\theta) is a Quadratic function
         - quadratic function can be visulaised through convex
         
