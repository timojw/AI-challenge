# Delivery

## Date & Location
Date: 11-12-2023

Location: House Stakeholder, Eersel

## Objective
I have made a application using HTML and CSS for front-end and Python with Flask for the back-end.
The objective is to present the application to the stakeholder, demonstrating its capabilities and limitations, and to receive feedback.

## Setup
The application set up on my local device.

## Agenda
1. Introduction - 2 min.
    I will start off by talking about the application's purpose and main functions. I'll give the stakeholder a quick run-through of our plan for the demonstration, so he;s well informed about what's going to happen.

2. Demonstration - 5 min.
    Then, I'll guide the stakeholder through the app, showing off its interface and features. We'll input some example data together to see how the app predicts outcomes. If the results aren't quite right, I'll explain why that might be. The stakeholder will also have a chance to enter their own data, like weight and age, and we'll see how the app predicts their strength in exercises like squats and bench presses. This will be a good opportunity to discuss whether the app's predictions are accurate and why they might not be.

3. Discussion on Model's Flaws - 5 min.
    After that, we'll focus on areas where the app needs improvement. I'll revisit its shortcomings and suggest how we might enhance its performance.

4. Feedback Session - 2 min.
    To conclude, I'll ask the stakeholder for their thoughts and feedback. It's important to hear what they liked and what they think could be better. Their input is crucial for refining the app.

## Demonstration Video

![](./templates/demo.mov)
[Video Youtube Link](https://youtu.be/rdBJ-ULSQTM)

## Stakeholder Profile
The stakeholder is Lars, he was also the stakeholder for the project. He goes to the gym on a regular basis, and is quite knowledgeable on the subject.

## Feedback
**Model Understanding:**
The stakeholder has a good understanding on how the model works and the logic behind results after certain inputs. So for example it is clear that when he selects a age lower than 18 or higher than 80 the accuracy of the model goes down significantly because it has had less training data for those age-groups. There were other situations like this discussed as well. He also understands what the reasons are for the low accuracy scores of the models.

**Feature Understanding:**
The stakeholder understands all the features and that certain features weight higher towards the final prediction. For example, sex and bodyweight are more important than age. There was no real need to go into great detail explaining the features and their relation to the target variable, because it is pretty straightforward and as a weightlifter he already had a great understanding on the features and their relations.

**Impact Assessment:**
Because of the mid accuracy the impact of this model will now be high when making actual informed decisions on what weight he should be able to lift. So first of all to make the model have an actual impact the first course of action would be to increase the accuracy. Also right now the model is bad at predicting the 1RM for people with data that is different to others.

## Reflection
In undertaking this AI project, I encountered significant challenges that highlighted areas for improvement. Firstly, the accuracy of my models was suboptimal, averaging around 55-60%.

A critical non-technical issue was time management. My tendency to procrastinate resulted in a compressed timeline, forcing me to complete substantial work as the deadline approached. This aspect of my work ethic requires significant improvement to ensure more efficient and less stressful project execution in the future.

On the technical front, a major difficulty was selecting an appropriate predictive model. The data presented complex relationships between features and the target variable, which did not conform to standard patterns like linear or polynomial correlations. This complexity necessitated a more difficult approach to model selection.

Finally, the current dataset may be insufficient for achieving high accuracy. I believe incorporating additional features, such as muscle mass, nutritional habits, and body length, could significantly enhance the predictive capabilities of the models. This expanded dataset might provide a more comprehensive understanding of the underlying patterns and relationships, leading to more accurate predictions.