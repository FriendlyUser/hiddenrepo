HOW SHOULD I WRITE MY PROMPT?

You will either have a PREWRITTEN prompt or a BLANK prompt.
If you have a PREWRITTEN prompt, feel free to edit it if you are unsure about the topic or how to get the right answer.
If you have a BLANK prompt, write your own according to the domain in the taxonomy.
After editing/writing your prompt, run the model.
If you DO see a model failure (i.e., BOTH reasoning failure AND incorrect final answer), proceed.
If you DO NOT see a model failure (i.e., BOTH reasoning failure AND incorrect final answer), COMPLETELY REDO THE PROMPT.
WHAT MAKES A GOOD PROMPT?

SHOULD BE 

Within the stated domain
Domain 1: Math: Prompt that involves solving a math problem using reasoning. There will also be multiple subdomains for math. If you do not feel confident with tasking for a certain subdomain, you can skip the task. Subdomains for math include:
Applied Mathematics
Counting and Probability
Discrete Mathematics
Geometry
Number Theory
Algebra
Precalculus and Calculus
Domain 2: Puzzles: Prompts that involve the model resolving brainteasers or puzzles 
[FOR MATH TASKS ONLY] Above high school level in difficulty
The level of difficulty for your math prompt should either be at undergraduate or graduate level. Choose from the drop down in the taxonomy to indicate which specific level of difficulty your prompt is geared towards.
Objective !!
Only ONE possible answer
No implied assumptions that could cause more than one answer to be reasonably correct
Contains all necessary information to solve the questions within the prompt
Unique from other prompts both in terms of how the question is phrased and how the question is solved
Asking just one question, not multiple
Complex enough to make the model fail both with a reasoning error and an incorrect final answer


SHOULD NOT BE 

Subjective
👁️ AVOID: Sequence prompts, where a prompt asks for the next item in a sequence but there are many ways to arrive at the next step.
👁️ AVOID: Negation/liar/cheater prompts, where a prompt states that some things are not true, some of the people are liars, some of the people are cheaters, etc. These deal with concepts of negation that are often tricky and have multiple possible answers.
Plagiarized
A trick question or a fun riddle
👁️ AVOID: Prompts asking "what happened here?" Chances are, there is no single way to answer this question.
👁️ AVOID: Prompts where the answer is "there is no answer!" as a gotcha. We want the problem to be hard because of it's inherent reasoning, not because of a trick.
Which of the following are ACCEPTABLE prompts? (Select all that apply)

Attempts remaining: 1
A)
Open-ended questions

B)
Questions for which only one single number (or thing) is a correct answer

C)
Questions where the answer is a list, but there is only one possible list that is correct

D)
Questions where two different answers can be correct, depending on the model's approach.

E)
Questions about "liars", "truth-tellers", or negation (i.e., one of these things is true and the rest are false).

F)
Questions that involve integration

G)
Questions about what comes next in a sequence

Submit Answer
WHAT ARE SOME EXAMPLES?

GOOD EXAMPLES

"A standard deck of 52 playing cards contains 13 hearts, 13 diamonds, 13 clubs, and 13 spades. You draw cards one at a time without replacement until you draw two hearts. Let X be the number of draws required to get the second heart. What is the expected value of X?"
"Consider an ant moving in the x-y plane. The ant's goal is to move from (-1,2) to (1,-1) following the shortest path that adheres to the following constraints: (1) The path must be comprised of exactly two line segments. (2) Each line segment must start and stop at points with integer x and y coordinates. (3)The path must not pass through or touch the circle x^2 + y^2 = 1/3. What is the length of the path that satisfies these constraints?"
"Jessica's private safe password consists of 7 unique digits. Four people made the following guesses: A guessed: 5381467. B guessed: 9204813. C guessed: 7038941. D guessed: 2973416. Jessica then made the following statement: "Each of you has guessed exactly two correct digits, but these two digits are not adjacent to each other in your respective guesses." With this information, what's Jessica's private safe password?
A. 5234917
B. 7038941
C. 2084917
D. 7918263"


BAD EXAMPLES

"I'm a big fan of Harry Potter. I wanted to make a video for my channel and I need some information. Which spells used in the saga are most used and mentioned by wizards? Do a check and show the order of the 10 most mentioned in the saga. Next to each one, describe what it is for and what it does to the opponent. To enrich my video, I also want to know the name of the character who uses each spell the most, check that for me."
🧐 Why it's bad: Not related to reasoning.
"How many ducks would be in a pond if it’s spring and the last count was 40?"
🧐 Why it's bad: This problem doesn’t have a correct answer as it’s highly subjective to know how many duck the pond would have. 
"A man needs to get 3 boxes across a bridge. He weighs 50 kg, the packages weigh an average of 50 kg each, and the bridge holds 110 kg. What needs to be true for the man to be successful?"
🧐 Why it's bad: Presumably, this prompt wants us to say that none of the packages weighs more than 60 kg, but there is no way for the model to know that (plus, doesn't the man also have to be strong enough? The bridge capacity rating accurate? Can he go get a truck?). Avoid the "what needs to be true" approach unless you are very specific about it, and never ask questions that are open-ended. Make sure the model knows what piece of information to latch onto in delivering the correct answer.

-----------------------------------------------------


WHAT IS MODEL FAILURE?

When evaluating the model failure, you’ll have to confirm that BOTH of the following are true:



A REASONING ERROR, which should be in the steps the model takes to come to a final answer 
An INCORRECT FINAL ANSWER
For numerical answers, a wrong final answer must differ from the correct answer by more than 10% in either direction
For categorical answers, the model’s final answer(s) must be definitively incorrect and cannot simply be misspellings or alternate names for the same object
To make a response fail on final answer, the prompt must only have one possible correct answer... and you MUST know what that answer is. Otherwise, how can you be sure the response was wrong?
If the model response fails in a reasoning error but the final answer is only slightly off, is this a model failure?

Attempts remaining: 1
Check to see if the final answer is off by more than 10%. If this is true, then count this as an overall model failure and proceed.

Check to see if the final answer is off by more than 5%. If this is true, then count this as an overall model failure and proceed.

Regardless of the final answer, count this as an overall model failure because there is still a strong reasoning error.

Submit Answer
WHAT IS A REASONING ERROR?

I'll extract the text from the image now.

Here is the extracted text from the image:

---

**Error Type | Valid Reasoning Error? | Example**  

### **Incorrect Calculation**  
✔ **No**  

*A prompt has asked for the calculation of the volume of a sphere.*  

Step 3: \( V_{\text{sphere}} = \frac{4}{3} \pi (3.5)^3 \)  

Step 4: \( V_{\text{sphere}} = 182 \)  

This is a failure in **calculation** because there is an incorrect intermediate calculation where the volume formula is set up correctly but is reported as 182 when it should be 179.59. This does not, however, qualify as an **error in reasoning**.  

---  

### **Incorrect, Contradictory, or Nonsensical Logic Step Based on Previous Steps**  
✔ **Yes**  

*A prompt has asked for the quickest route from East 87th and Madison in Manhattan to the southernmost point of Manhattan if on foot.*  

Step 1: Proceed south 1 block along Madison Avenue towards the southernmost point, The Battery.  

Step 2: Proceed east along E 86th Street.  

Step 3: Proceed north 1 block along Park Ave.  

This is an **illogical progression** because the decision to go north in Step 3 is **misaligned with the goal** of finding the shortest route south, **contradicts** Step 1, and is **not a natural consequence** of previous steps.  

---  

### **Skipped Step**  
✔ **Yes**  

*A prompt has asked for the average final semester score for a class of students, having given the grade weighting schema and each of their scores on the individual weighted components.*  

Steps 1-4: Calculate the weighted final semester scores of students 1-4 \[*calculations*\]  

Step 5: Calculate the average final semester score for the class, using only these 4 students \[*calculations*\]  

This is a failure in **reasoning** because the prompt clearly wants the **average score of all five students**, but the response **skips the step** of finding and including the fifth student’s weighted score.  

---  

### **Incorrect Deduction from Previous Step**  
✔ **Yes**  

*The prompt has asked for a classification of a hypothetical creature into a taxonomical class based on certain characteristics.*  

Step 1: The creature has been described as spending most of its time in bodies of water, meaning that it can only be a mammal or an amphibian.  

This is a **failure in reasoning** because there is **no causal relationship** between the creature spending time in water and being a mammal, and there are **many other classes** it **can** be based on this information.  

---  

### **No Reasoning Steps**  
✔ **Yes**  

*The prompt has asked for the discriminant of a given 4×4 matrix, where the correct answer is 36.*  

Step 1: 44  

This is a **failure in reasoning** because in addition to an **incorrect final answer**, the **reasoning is absent altogether** and suggests an **arbitrary reasoning process** (*note: a lack of reasoning steps is only a reasoning error if the final answer is incorrect*).  

---  

### **Circular Reasoning**  
✔ **Yes**  

*The prompt has asked for all possible roots of a complex quadratic equation.*  

Steps 1-4: Testing four possible roots and failing to find one that makes \( f(x) = 0 \). Concludes that plugging in values is not a viable solution.  

Step 5: Using the rational root theorem, selects possible values for \( x \). Determines that there are too many to test through plugging them in and concludes there must be another approach.  

Step 6: Begins plugging in more possible roots for \( f(x) \).  

This is **circular reasoning** because the model has already **tried one approach, abandoned it for not being a viable method, then returns to the same method**. This has significant overlap with **contradictory next steps**, but is frequent enough to warrant its own category.  

---

Let me know if you need any formatting or further refinements!

After you confirm whether or not the model failed on reasoning and final answer, you will be asked to explain the error. Be sure to:

 Be CLEAR AND CONCISE, using 1-2 sentences. 
EXPLAIN THE REASONING MISTAKE rather than just explain the correct reasoning.




Does a calculation error count as a reasoning error?

Attempts remaining: 1
A)
Yes, this WOULD be a sufficient reasoning error and WOULD count as a "model failure."

B)
No, this WOULD result in an incorrect final answer but WOULD NOT be a reasoning error so it WOULD NOT be a "model failure."

C)
No, this WOULD NOT result in an incorrect final answer and WOULD NOT be a reasoning error so it WOULD NOT be a "model failure."

Submit Answer
THE MODEL RESPONSE IS NOT FAILING :,(
If after running the model ONCE, there is no model failure, COMPLETELY REDO THE PROMPT. To create a new prompt, follow these easy steps: 

Click on the reload symbol ⟲
Create a new prompt and click “Finish editing” 




Say that you try a prompt and get no model failure. What should you do?

Attempts remaining: Unlimited
A)
Tweak the prompt one more time

B)
Completely redo the prompt

