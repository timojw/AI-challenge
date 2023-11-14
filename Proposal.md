# Domain Understanding
**Domain understanding is a fundamental aspect of AI project development, pivotal in shaping the direction, effectiveness, and relevance of the solutions provided. AI, as defined by Spruit & Lytras (2018), is not just about the creation of analytical systems but is deeply rooted in the enhancement of the daily practices of domain experts. This enhancement necessitates a profound comprehension of the domain in question, attainable only through meticulous exploratory research.**

## Understanding One Rep Max (1RM)
One Rep Max (1RM) is a cornerstone concept in weightlifting and strength training, representing the maximum amount of weight a person can lift for one repetition of a given exercise. It's a crucial metric, not just as a measure of strength, but also as a tool for structuring and progressing training programs.

In the realm of weightlifting, 1RM is defined as the heaviest weight that can be lifted once with proper form. It is a direct measure of the maximal strength a person possesses for a specific exercise, like a squat, deadlift, or bench press. This metric is pivotal as it provides a clear and quantifiable benchmark of an individual's strength capabilities, serving as a foundation for setting training goals and tracking progress over time.

Calculating 1RM can be done in two primary ways: direct measurement and estimation. The direct method involves physically lifting the heaviest weight possible for one repetition. While this approach is accurate, it's often impractical and risky, especially for inexperienced lifters. To mitigate these risks, several estimation methods have been developed. These involve lifting a submaximal weight for multiple repetitions and then using mathematical formulas to estimate the 1RM. The most common of these formulas include the Epley Formula and the Brzycki Formula, which use the number of repetitions performed with a certain weight to estimate 1RM.

However, these estimation methods have their limitations. They can be less accurate for those with less lifting experience or for very high or low repetition ranges. The accuracy also varies depending on the specific exercise being performed. Despite these limitations, estimated 1RM is widely used because of its practicality and safety.

The significance of 1RM in weightlifting extends beyond a simple measure of strength. It's intimately linked with training intensity and progression. For instance, many strength training programs prescribe exercises based on a percentage of an individual's 1RM. This allows for a tailored approach to training intensity, ensuring that the workouts are challenging yet achievable, and most importantly, safe.

Moreover, 1RM plays a critical role in designing weightlifting programs. It aids in the creation of periodized training plans, which are structured to vary intensity and volume over time to maximize gains while minimizing the risk of overtraining and injury. By regularly assessing and updating an individual's 1RM, trainers and athletes can adjust training loads to align with improvements in strength, ensuring continual progression and adaptation.

In summary, 1RM serves as a vital benchmark in weightlifting, offering a clear and objective measure of an athlete's maximal strength. Its role in calculating training intensity, monitoring progress, and designing effective weightlifting programs underscores its importance in the world of strength training. Despite the challenges in its calculation, 1RM remains a key metric for athletes and trainers alike, providing a foundation upon which to build and refine strength training regimens.

### 1RM as a Target Variable in AI Models
Choosing 1RM (One Rep Max) as a target variable in AI models for weightlifting and strength training is particularly insightful due to its quantifiable and objective nature. As a measure of the maximum weight a person can lift in a single repetition, 1RM provides a clear, numerical benchmark of an individual's strength. This straightforward quantification makes it an ideal candidate for AI modeling, as it offers a precise target for prediction and analysis.

How does 1RM serve as a quantifiable and objective measure of strength?
What insights can be derived from analyzing 1RM data?
Predicting 1RM: Applications and Challenges

What are the potential applications of predicting 1RM through AI?
What challenges arise in modeling and predicting 1RM accurately?

### The Role of Features in Predicting 1RM
In the context of strength training and 1RM, understanding how various factors like age, gender, weight, height, and other personal attributes influence performance is crucial. This understanding becomes particularly relevant when considering the profile of a 20-year-old male who is actively engaged in weightlifting, with specific fitness goals centered around muscle building and strength enhancement.

**Age and Strength:**
Age is a significant factor in strength training. In general, individuals in their late teens to late twenties, like our 20-year-old gym enthusiast, are often at a prime age for muscle development and strength gains. During these years, the body's response to resistance training is typically at its peak, making it an ideal time to focus on increasing 1RM. However, it's also important to recognize that as one ages, natural changes in muscle composition and recovery rates can impact the ability to sustain and improve 1RM. Thus, for someone in their early twenties, capitalizing on this phase for muscle building and strength training is both timely and beneficial.

**Gender Differences in Strength:**
Physiological differences between genders play a crucial role in strength and 1RM. Men, typically, have a higher proportion of muscle mass due to hormonal differences, notably higher testosterone levels, which contribute to greater muscle hypertrophy and strength gains. This is particularly pertinent for our subject, as his gender aligns with these physiological advantages, potentially allowing for more significant improvements in specific areas like the chest, back, and arms, which he aims to develop.

**Impact of Weight and Body Composition:**
Body weight and composition are critical in determining 1RM. Generally, a higher body weight, provided it's accompanied by proportional muscle mass, can contribute to lifting heavier weights. However, for our 20-year-old, weighing 71 kg with a BMI of 21.4, the focus might be on gaining muscle mass to improve his 1RM. While his current weight provides a good foundation, increasing muscle mass through targeted training and nutrition will be essential for enhancing his 1RM.

**Role of Height in Lifting Performance:**
Height can influence 1RM, but its impact varies based on the exercise. For taller individuals, some exercises like deadlifts may offer mechanical advantages, whereas others like squats might present more of a challenge due to the greater range of motion required. At 182 cm, our subject's height falls within a range that offers both advantages and challenges in weightlifting, necessitating a tailored approach to training that maximizes his biomechanical strengths.

**Other Influential Factors:**
Other aspects like training experience, muscle composition, and nutrition significantly affect 1RM. Given that our subject is very active, enjoys weightlifting, and has access to gym facilities, he is well-positioned to make progressive strength gains. His preference for structured routines mixed with varied workouts aligns well with the principles of progressive overload and adaptation, essential for improving 1RM. Furthermore, his commitment to a balanced diet with adequate protein intake will support muscle recovery and growth, directly impacting his 1RM potential.

## Interview with the Stakeholder
**The purpose of this interview is to gain a comprehensive understanding of the fitness habits, goals, and preferences of a young man deeply engaged in weightlifting. This information is crucial for tailoring a personalized machine learning algorithm that delivers a sort of training schedule that aligns with his specific needs and objectives. There is also some general information that needs to be gathered.**

### General Information
1. **Gender:** Male
2. **Age:** 20
3. **Length (Height):** 182 cm
4. **Weight:** 71 kg
5. **BMI:** 21.4

### Personal Fitness Goals and Preferences
1. **Primary Fitness Goals:** 
   - *Response:* My primary fitness goals are to build muscle and increase overall strength.

2. **Focus Areas in Bodybuilding:**
   - *Response:* I want to focus on developing my chest, back, and arms as specific muscle groups.

3. **Preferred Types of Exercise:**
   - *Response:* I enjoy weightlifting and strength training exercises. I find it satisfying to challenge myself with heavy weights and progressive resistance.

4. **Disliked Exercises:**
   - *Response:* I dislike long bouts of cardio but understand the importance of cardio health, so I'm willing to incorporate shorter cardio sessions.

5. **Medical Conditions and Physical Limitations:**
   - *Response:* I don't have any pre-existing medical conditions, but I might need to be cautious about proper form and technique to prevent injuries.

6. **Current Physical Activity Level:**
   - *Response:* I consider myself very active due to my regular gym workouts and an active lifestyle.

7. **Access to Exercise Equipment:**
   - *Response:* I have access to a gym; I have equipment at home, but I prefer using gym equipment for my workouts.

8. **Preferred Duration of Workout Sessions:**
   - *Response:* I prefer my workout sessions to be around 60-90 minutes.

9. **Preference for Solo or Group Workouts:**
   - *Response:* I usually work out alone but occasionally enjoy working out with friends who share similar fitness goals.

10. **Workout Frequency:**
    - *Response:* I'm willing to dedicate about 5-6 days a week to exercise.

11. **Preferred Workout Structure:**
    - *Response:* I prefer a mix of structured routines and varied workouts to keep it interesting and challenging.

12. **Interest in Special Training Programs:**
    - *Response:* I'd like to include strength training as the primary focus, but I'm open to incorporating occasional high-intensity interval training (HIIT) for cardio and flexibility workouts for better overall performance.

13. **Progress Tracking Preferences:**
    - *Response:* I prefer to track my progress through tracking my lifting stats.

14. **Dietary Considerations:**
    - *Response:* I aim to maintain a balanced and nutritious diet with adequate protein intake to support muscle growth.

15. **Preferred Time for Exercise:**
    - *Response:* I prefer to work out in the early morning as I feel more energized during the day after the workout.

## Project Scope
**Defining the scope of this project is essential to set clear boundaries and expectations.**

Central to the project is the calculation of a one-time One Rep Max (1RM) for the subject, a 20-year-old male weightlifting enthusiast. It is important to note that this 1RM will be applied uniformly across all exercises, an approach that simplifies the process but admittedly does not account for variations in strength across different muscle groups. This assumption, while not entirely realistic, is a necessary compromise given the project's constraints and objectives.

Another crucial aspect of the project scope is the decision to exclude nutrition from our considerations. While nutrition undeniably plays a significant role in fitness and strength training, its complexities and the need for highly individualized information make it beyond the purview of this specific project. This exclusion is a strategic choice to maintain focus and manageability.

Additionally, it's important to clarify that the conversion of the calculated 1RM into a detailed training schedule is not included in the project scope. While the 1RM provides a foundational metric, the development of a tailored training regimen based on this value falls to the stakeholder. They have the option to utilize various available calculators and formulas to translate the 1RM into a practical workout plan. This delineation ensures the project remains focused and achievable within its defined parameters.

In summary, the project will concentrate on establishing a baseline strength level through a one-time 1RM calculation, while consciously setting aside the aspects of individual muscle strength variability and nutrition. Additionally, the application of 1RM in creating a workout schedule, though critical, is designated as a task for the stakeholder, allowing the project to maintain a clear and focused scope.

## TICT

# Data Sourcing

# Analytic Approach

# Sources