
For the following rubrices dos and dont

✅ High-Level Tips





Do!
Don’t
Prompt
Want to stick to the assigned category for the prompt
Want the prompt to be specific and answerable 
To include 1+ constraints
Re-generate/increase the complexity of your prompt if it doesn’t fail
Choose a different category, you must stick to your category
Have proofreading errors or poor english
Don’t pick something out of your expertise or that is too hard to assess in terms of the response
First Response
Ensure that it fails an objective way at one of the rating criteria (preferably instruction following or accuracy) and that 9/10 of people would agree with you
Spend time and be thorough on the ratings → make sure that you write your justifications in a way that helps the reviewer understand the issues you saw
If the response doesn’t fail, adapt your prompt with an additional constraint or increased scope to make it fail
Not fact check!!!
Don’t select responses where theres a ton of complex/hard fact checking involved
“Make up an error” → be intellectually and pick obvious/major issues
Second Prompt
THE SAME INSTRUCTION AND INTENT AS THE FIRST PROMPT! BUT ADDING STUFF TO HELP THE MODEL CORRECT ITS RESPONSE!
Guide the model to correct the core issues
Guide the model to keep what it did well/what you can leverage to reduce fact-checking


Change the core request/constraints
Second Response
Make the response stand-alone (i.e. remove references to Turn 1)
Remove something like (“You’re right, my apologies!”)
Be thorough in checking the new response


Not fact-check the response
Not manually fix it


Rating
Purposefully  rate response 1 vs response 2
Revise your rewrite if you feel that the rewrite/guided is not better than the first response
Write a thorough justification explaining:
Your verdict
Why the response is better
Specifically what it does better on 
TRIPLE CHECK YOU’RE REFERENCING THE RIGHT RESPONSE (CHECK THAT RESPONE 1 AND RESPONSE 2) ARE WHAT THEY ARE. 
Don’t pick “no preference” since that means the model didn’t fail → re-do the task
Generic in your justification




And for  the following instructions

Starfish Mint v2 Tasking Handbook
Last Updated: Oct 23, 2024

This document is meant to be used when you first onboard the project to learn everything you need. You should read this document thoroughly. 

Tasking Checklist:Starfish Rubrics Do's and Don'ts
Common Errors: Starfish RTL - Common Errors
Reviewer SOP: Starfish Mint V2 Reviewer SOP

Task Walkthrough Video: https://www.loom.com/share/2885f42057c14f0cb43248092192ff64?sid=4a055e77-8e9c-48a4-9f8f-725380c0a074
Office Hours: 
Monday - Friday: 
10:30 AM - 12:30 PM PDT
6:00 PM - 7:00 PM PDT
https://meet.google.com/aqq-djzs-kmz 


🔭 What is this project all about?
🗺️ Tasking Workflow
📐 Task Specifications
Review the Instructions
✍️Prompt Writing
🔍 Evaluating Model Response
✅How to evaluate a model response?
✍️ Generate a perfect response
☀️ Deep Dive: Response Rating Dimensions
Final Step - Side by Side Rating and Justification
For Reviewers - Workflow and Task Rating Rubric
📚 Appendix


🔭 What is this project all about?


🍎 Learning Outcomes of this Section

Familiarize yourself with the outline of the task and its components
Understand why we’re doing this project in the first place



Welcome to Starfish! In this project, you will create data that will teach the model how to identify bad responses and produce good ones. Let’s break down the task workflow and things that we consider important and then explain why each one is important!

Task specifications:

Write a prompt that makes the model fail
You want to write a prompt that makes the model fail in a certain dimension such as instruction following or truthfulness
Why: by making the model fail, you’re targeting an area the model is weak at! This means your data meaningfully improves the model! Think about it, why would we provide data on things the model is good at? For example, if I’m very good at washing dishes, I won’t learn much if you show me videos on how to wash dishes. However, if I’m very bad at painting my walls, and you show me a tutorial of how to do it well, then I’ll likely get much better at painting and therefore improve my overall skills!

Follow the category assigned and annotate the topic
Why: you help us understand the diversity of our dataset, which is key to improving the model! We need diverse datasets in our deliveries!

Rate the poor response on a series of dimensions
You will indicate which dimensions the model has an issue on and explain why.
Why: by telling the model exactly where it was wrong and explaining why, you’re helping it actually identify the issue correctly, which helps it improve. For example, if my golf swing is bad, and you tell me “your golf swing is bad”, I don’t know what needs fixing. But if you specifically tell me “it’s bad because your grip is wrong”, then I’m more likely to improve.

Improve the model response through guiding it and manually fixing
You will use the model itself and tell it how to rewrite the response to fix the issues, and if still doesn’t get it, you can manually fix it!
Why: through doing this you’re showing the model what a great response looks like! Now, it sees two response to the same prompt, the first which shows it what not to do and the second shows it what to do.

Perform a side by side ranking and explain why one response is better than the other
At this point, it’s clear that the response you wrote is much better (if you performed the task correctly). Now, you rate how much better it is and justify why.
Why: a high quality justification helps the model understand what makes the better response ‘better’ and how to distinguish between different responses to the same prompt!

🗺️ Tasking Workflow
In all, the general task workflow involves:
Write a prompt that produces a poor-quality response from the model in some way (e.g., instruction following, truthfulness, harmlessness).
Evaluate the Model’s Response
Once the model generates a response to your prompt, review it carefully. Identify areas where the response falls short or makes mistakes.
If the model does not have an issue, edit your prompt and try again until you make the model fail
Once you find a response that failed, you will rate it on specific dimensions (e.g. instruction following, truthfulness, harmlessness)
“Find” or create a good response for this prompt
Guide the model to provide a good response by telling it where it made a mistake and giving it hints to produce an error-free response
Then, you will rewrite and fix the response directly 
Provide an explanation and side-by-side rating 
Finally, you'll compare the poor-quality response with the improved, corrected one. You will write a great justification that illustrates why the response is bad
This side-by-side comparison helps illustrate the improvements and supports further training of the model


📐 Task Specifications
Sections:
Review the Instructions
🚴 Turns
Prompt Writing
Evaluating model response
Generating a perfect response 
How to evaluate a model response?
Deep Dive: Response Rating Dimensions
Final Step - Side by Side Rating and Justification
For Reviewers - Workflow and Task Rating Rubric
Review the Instructions
Read the task carefully
Ensure prompt matches the given category and subcategory
Aim for diversity - Create prompts that bring in unique variations to avoid repetition. 
🚴 Turns
⭐ Concept: Turns

On many projects, turns refers to the pair of question-and-answer in a back-and-forth conversation you have with a model. So turn #1 is your initial request and the model’s response, turn #2 is your follow up, and so on.

On this project, turns are different! Turn #1 is still your initial request and the model response, but you need to think of Turn #2 as a revision of Turn  #1. It’s advised to think of each turn by its goal .

Goal of Turn #1:
Write a prompt that makes the model fail
Rate the poor response

Goal of Turn #2:
Write a new prompt built on prompt #1 that guides the response to reproduce the same response but fix the issues
Manually improve the new response
Justify why this response is better than the initial response




✍️Prompt Writing
⭐Purpose 
Your job now will be to write a prompt that: 

Always align with the category and subcategory description provided in the task.

Causes a model failure (a bad response from the model). 
This is an iterative process. You will be required to keep generating a new model response by rewriting prompts until you can cause a model failure. 
There is no maximum number of iterations allowed 
Ensure prompts sound natural, as if you were asking an LLM directly. 
Avoid using:
Pleasantries
Background context
Ensure prompts sound natural, as if you were asking an LLM directly. Avoid using:
Pleasantries
Background context



To start, let’s talk about what a User Prompt is composed of. Typically, User Prompts have three components:
Instruction: The instruction is your main request to the model, it dictates what the model says. Whether you ask it to explain inflation, write an email, or give a recipe, a perfect response will address the instruction completely, safely, and accurately.


Constraints: Constraints dictate how the model responds or talks. For example, if you ask for a recipe and specify "write it as a list" or "don’t use thyme because I’m allergic," you are constraining the response. A perfect response will follow these constraints while still addressing your instruction.
⭐ Concept: Instructions vs Constraints

The main difference between a constraint vs an instruction is how they affect the model response.
 
An instruction tells the AI what to do.
A constraint limits the AI’s degrees of freedom in some way.

Examples:
“Tell me about World War I.”
No constraint.
 
“Tell me about WW1. Do not mention France.”
One constraint.
 
“Tell me about WW1. Do not mention France or Germany.”
One constraint. The constraint has multiple elements but is still one constraint.
 
“Tell me about WW1. Do not mention France. Respond as a professor of military history who loves to talk about artillery.”
Two constraints.
 
“Write me a poem about WW1 in Shakespearean sonnet form. I may then ask you a follow-up question about France, which you should answer.”
One constraint. Sonnet form is the constraint. Notifying the AI that you will ask more questions does not constrain the AI’s responses.


When you're writing prompts, make sure they are clear, challenging, and natural. The goal is to maintain complexity while ensuring that the prompt is something you can assess confidently.
✍️How should you write this prompt?
Identify the Category and Subcategory in the task instructions. You should always follow the category that has been assigned in your task.
Task types
Open QA: Question-answering related to concepts defined in the prompt.
Closed QA: Question-answering related to source text.
Classification: Determine appropriate categories according to characteristic/shared quality.
Retrieval: Return relevant analysis or information based on a query.
Extraction: Identify key entities from a piece of text.
Assigned categories:
Structured Output: Ask for the model to generate data and structure it. For example, asking it to output its format as a list, as a table, or with certain markdown features.
Precise Instruction Following: A prompt with 3+ strong constraints. Pick constraints where it's clear whether the model follows them or not. For example, write a constraint about language style, content, engagement, length, expertise level, time sensitivity, formatting, structure, and exclusions.
Length-constrained Outputs: Add a prompt with length constraints and context for it. For example, a range essay between 150-300 words, character limit for a tweet, multi-level limits (i.e. 3 paragraphs. 4 sentences each, 10 words per sentence), and others.
Reasoning: Create common reasoning problems/math problems (pre-calculus, algebra, geometry, linear algebra, word problems, etc.)
Formulate a clear and logic prompt
There should be no ambiguity. Prompts should be clear, unambiguous, and not contrived.
Ensure you are confident about what the correct answer should be.
Introduce Specific Parameters and Constraints (see section here)
Purpose: Adds complexity and specificity to the prompt.
Action: Specify parameters and constraints for the model to follow.
Try to come up with a way to confuse or challenge the model, while still keeping things logical.
One approach is to add extra, irrelevant details or introduce an object or scenario that suggests something indirectly. This can lead the model to make a wrong assumption and give an incorrect answer. Another method is to use objects or situations with subtle characteristics that require deeper knowledge to fully understand, making it harder for the model to solve the problem correctly.
The ultimate intent is to create prompts that are challenging but still something you can verify easily. Each prompt should remain complex, while being written like something a natural user would say—even if that means using casual language or informal tone. The goal is to strike a balance between complexity and clarity, ensuring that the task is difficult for the model but straightforward for you to evaluate.



🌳 Guide to Writing Natural Prompts
One of the ways we'll improve our customer model with the data we provide is by training it on situations it will encounter in real life! To do that most effectively, we need our conversations to emulate real users' conversations with the model!
Your prompts should reflect how real users write—that is, informal punctuation, abbreviations, spelling and grammar mistakes, shorthands, slang, etc. are all welcomed—just write naturally as you would as a user, which often means writing quickly and casually!
In your prompts, you should:
Avoid Pleasantries: Avoid greetings, expressions of gratitude, or any unnecessary phrases like “please” or “thank you.” Focus on the request itself.
Examples of prompts with pleasantries: Hi! Could you please explain the concept of mindfulness in two paragraphs? Thanks in advance!
Good example: explain the concept of mindfulness in two paragraphs
Avoid Background Information/Context: Don’t include explanations, context, or reasons for asking. The prompt should focus solely on the specific task or question.
Example of prompts with background information/context: Lately, I’ve been trying to incorporate mindfulness into my daily routine because I’ve read a lot about its benefits for mental health and focus. I want to make sure I fully understand what it really means, so I was wondering if you could explain it for me in two paragraphs. I’m looking for a clear, concise explanation so I can apply it better in my life.
Good example: could you explain mindfulness to mental health in 2 paragraphs
Avoid overly formal language
Examples of prompts with overly formal or overly casual language: Would you be so kind as to elucidate the intricacies of mindfulness by composing two paragraphs of text, each containing a precise number of three sentences?
Good example: ﻿explain the concept of mindfulness in two paragraphs

📋Before submitting your task, make sure your prompt hits all the points on this checklist:
No pleasantries
No background info or extra context
No overly formal language
Keep prompts natural
Use abbreviations and shorthand where it fits
Allow minor spelling/grammar mistakes naturally
Use slang, but in moderation

🚫 What to avoid:
Over-the-top slang
Prompts that are too casual or unnatural
Losing clarity just to sound casual


✍️Examples of Acceptable Prompts: 
Good prompts: 
Bad prompts: 
Describe the taste of coffee using no more than 30 words.

Why is it a good prompt?
This prompt is clear, stating exactly what should be described ("taste of coffee") and setting a specific word limit (30 words). There is no ambiguity, and the focus is clear.
Describe the taste of something you drink.


 Why is it a bad prompt?
This is vague and doesn't specify what "something" is. There are no constraints and will likely not lead to a failed model response in the first turn.
Explain why climate change has been accelerating in recent years, using bullet points with a maximum of 10 points. Include specific examples from the U.S. to highlight the impact.

Why is it a good prompt?
Prompt it’s clear and focused, asking for an explanation of recent climate change acceleration in an organized way using bullet points. It encourages concise answers while also including specific U.S. examples to make the explanation more grounded and relevant. 
The number of bullet points are specified, leaving no room for misinterpretation.
List seven things that describe a scene. 


Why is it a bad prompt?
This is unclear and doesn't specify "sunset" or the character limit. There are no constraints and will likely not lead to a failed model response in the first turn.
Explain your understanding of mindfulness in precisely two paragraphs with three sentences each.

Why is it a good prompt?
This prompt gives clear constraints: two paragraphs with exactly three sentences each. It defines both the content (mindfulness) and the form (two paragraphs, three sentences), removing any confusion about expectations.
Write an explanation of mindfulness. 



Why is it a bad prompt?
This lacks clarity on the required structure and is too open-ended.


🔍 Evaluating Model Response
Once you’ve written this prompt, check that it causes a bad response. 

Check that the prompt written has caused the model to fail to answer as intended. 
If the model fails to answer correctly → no further action is required on the prompt. ✅
If the model does answer the prompt correctly → create another prompt until you are able to cause a failure. ♾️
How can I check for this?
Depending on your prompt and category it may be easy to spot if the model response is wrong, but sometimes it may not be easy.
Run fact checks if you are not sure about the answer, but keep in mind DO NOT OVER DO IT, typically incorrect model responses should be obvious and important. 



✅How to evaluate a model response?
You will be evaluating a model response against the following dimensions: Instruction Following, Accuracy, Harmlessness Content, Conciseness & Relevance, Completeness, Writing Style & Tone. 
Dimensions
Step-by-Step
Instruction Following
Step 1: Review the instructions provided. Carefully read the original prompt to understand exactly what was asked. Make sure there is no ambiguity.
Step 2: Compare the response to the instructions and constraints. Does the response address every part of the prompt? Identify if any parts were ignored or misunderstood.
Step 3: Check for adherence to constraints. If there were specific guidelines (word count, format, structure), verify whether these were followed exactly.
Step 4: Determine clarity of adherence. Assess if the response followed the instructions without misinterpretation or unnecessary additions that deviate from the task.
Accuracy/Truthfulness
Step 1: Identify the factual claims. Highlight any statements that rely on factual information.

Step 2: Verify the facts. Check the accuracy of the information by cross-referencing reliable sources or using your own knowledge. 

Step 3: Evaluate correct application. Ensure that the correct facts are applied properly in the context of the response. Misapplied facts can be as misleading as incorrect ones.

Step 4: Identify potential errors. If any part of the response includes inaccurate or misleading information, mark those areas as inaccuracies.
Harmlessness
Step 1: Scan for potentially harmful content. Review the response for any language or information that could cause harm—either physical, emotional, or social harm to individuals or groups.

Step 2: Consider sensitive topics. Evaluate whether the response discusses sensitive issues (e.g., race, gender, politics) in a respectful and neutral way.

Step 3: Check for offensive language. Ensure the response avoids offensive, discriminatory, or inappropriate language.

Step 4: Assess tone for bias. Ensure that the tone does not propagate stereotypes, spread misinformation, or unintentionally encourage harmful behavior.
Content Conciseness & Relevance
Step 1: Highlight the key points. Identify the main points or arguments presented in the response.

Step 2: Check for unnecessary information. Look for sentences or sections that don't contribute to the overall point or that repeat earlier information.

Step 3: Evaluate relevance. Ensure that all the information provided is directly related to the prompt and doesn’t stray off-topic.

Step 4: Measure wordiness. Evaluate if the response is unnecessarily long, using more words than needed to convey a point. The response should be concise while remaining informative.
Completeness
Step 1: Examine all parts of the prompt. Ensure that every part of the prompt or question has been fully addressed.

Step 2: Check for missing details. If a detailed explanation or reasoning was requested, confirm that the response provides sufficient depth and doesn’t leave important aspects unexplained.

Step 3: Evaluate balance. Ensure that no section is disproportionately detailed compared to others, leading to incomplete treatment of the question.

Step 4: Assess if further elaboration is needed. If there are gaps or vague areas, note where the response needs more detail to be fully complete.
Writing Style & Tone
Step 1: Identify the required style/tone. Determine if the original instruction asked for a specific writing style (e.g., formal, casual) or tone (e.g., friendly, professional).

Step 2: Compare the style/tone. Check if the writing style and tone match the requirement. If no specific tone was requested, ensure the tone is appropriate for the context.

Step 3: Evaluate consistency. Make sure the tone remains consistent throughout the response. Sudden shifts in tone (e.g., from casual to formal) should be avoided unless explicitly required.

Step 4: Assess clarity and flow. Ensure that the writing is easy to follow, with clear transitions between ideas and no awkward phrasing. The sentences should flow smoothly and be grammatically correct.


Examples: 
Type
Prompt/Response
Explanation
Evident Issues / Easy
Prompt: 
Tell me how I can make some pasta dough without flour

Response: 
If you don't have any flour you can use some baking soda instead…
The response is incorrect because baking soda cannot be used as a substitute for flour when making pasta dough.
Subtle Issues / Medium
Prompt: 
When is the independence day of Congo

Response: 
The Independence Day of the Republic of the Congo is celebrated on August 15th. It marks the date in 1960
 There are two different countries of Congo, The Republic of the Congo and The Democratic Republic of the Congo. Model response is incorrect and it needs some fact checking
Hard
Prompt: 
What are the nutritional benefits of kale?

Response: 
Kale is very nutritious, containing high levels of vitamins A, C, and D, and is great for health.

Although kale does provide vitamin A and C, it doesn't contain any vitamin D, instead it contains vitamin K.


If the prompt does not produce an error in the response, keep rewriting the prompt until you encounter a failure (bad response). 
Use the ‘retry from chat’ at the top right to create another prompt and generate a new response.

Once you’ve confirmed that the response produces a failure, proceed to step 4 and Turn #2 of guiding the model to generate a better response. 




Turn #2
✍️ Generate a perfect response

In turn 2, you will now guide the model to generate a better response than it did with the initial response. There are a few ways to do this:

Make modification(s) to the original prompt in turn #2 prompt. 
Point out the errors the model made, and ask it to provide a new response taking these things into consideration. 
Remember that this is Turn #2, so the model already knows what happened in the prior turn. These modification(s) will help guide the model to write a better response; this is what we refer to as “guiding”.
The goal for this step is for you to be able to get the model to provide an ideal response purely through prompt engineering.
Note: You cannot take out any of the parameters/constraints from the prompt turn 1. You can only add additional constraints. 




🛞What is “Guiding the Response”?
Guiding the model means ‘steering’ it to give you the kind of answers you want. It’s basically your chance to produce the perfect response to the original prompt using an LLM! 

You can use this prompt space freely! For example, if I found the first response to write a great response on who the 10 last US presidents are, but the president in spot #9 was incorrect, I can just prompt it to output the list and replace the answer at #9 with the correct president.

Another way I can use it is by giving the model hints! For example, if the model didn’t output a format correctly, I can provide the model with an example on how to write in a certain format.

You do this by being clear about what you ask, like choosing a certain style or focusing on a specific topic. It’s like giving the model directions so it stays on track with your needs.

Strategies for steering: 
Use Clear Prompts 
Clearly state what you need and mention any specific details that are needed or missing. 
Example: Instead of asking "Tell me about solar energy," ask, "Can you explain the benefits of solar energy for residential homes?"
Use Follow-Up Instructions
Provide follow-up requests by specifying what was missing or what needs to change 
Example: “Can you make this explanation more formal?” or “Focus more on the environmental benefits.”
Guide Through Example
Provide examples for the model 
Example: If you want a certain format or structure, give the model an example to follow. “Format the output like this: 'Step 1: Overview, Step 2: Analysis, Step 3: Conclusion.'”

✅Step-by-Step on how to write a guiding prompt: 
Step 1: Review the Original Prompt and Response
Review the Initial Prompt: Start by re-reading the original prompt to ensure you fully understand what was asked. Make note of the constraints, format, or any specific details required.
Review the Model’s Response: Examine the model’s initial response carefully. Identify areas where it met the prompt’s requirements and where it fell short. Look for factual errors, formatting issues, missing details, or incorrect tone.
Step 2: Identify the Issues in the Response
List the Errors: Clearly identify the specific problems with the model’s response. 
Categorize the Errors: This helps in addressing them clearly. 
For example, if there’s a factual error, you would guide the model to correct the specific fact, or if the response is missing context, you guide the model to add it.
Step 3: Modify the Prompt
Keep the Original Constraints: You cannot remove any parameters from the original prompt. Make sure that all the original instructions are preserved even if you use a different approach.
Add Specific Follow-Up Instructions: Based on the errors identified, you now add additional constraints or directions that will guide the model to improve the response. You can:
Specify what needs fixing: For example, "Correct the information about solar panel efficiency, and ensure it reflects the most recent data."
Ask for elaboration: "Provide more detail on how residential solar panels work."
Focus on structure: "Make sure to list the steps in a numbered format."
Clarify tone/style: "Rewrite this section to make it more formal."
Be Specific and Clear: Avoid vague language. Clearly communicate what part of the response needs adjusting and what outcome you expect.
Step 4: Guide Through Examples (Optional)
Provide an Example Format: If the issue is related to structure or formatting, include an example of how you want the response to be structured. For instance:
Example: "Reformat the list of benefits into bullet points. Example format: '- Solar panels are cost-efficient.'"
Give a Reference: You can even provide a reference for tone or content if needed. 
For example: "Use a tone similar to the following: 'Solar energy is one of the most environmentally friendly options available.'"
Step 5: Add Additional Constraints (Optional)
If the original prompt didn’t specify enough detail, you can add constraints to get a more targeted response:
Focus on specifics: "Ensure that at least three benefits of solar energy are mentioned, with one focused on cost savings."
Limit word count: "Rewrite this answer in 150 words or fewer."
Change the perspective: "Write this response from the perspective of a homeowner considering solar panels."
Step 6: Test and Refine
Evaluate if the response now meets your expectations and refine if necessary. If the response is still not ideal, continue refining your guiding prompt by adding more precise constraints or examples until the output is satisfactory. Rewrite if necessary (refer to section below).



✍️How to rewrite the response to be perfect
A perfect response should be accurate and fully aligned with the prompt’s requests and constraints. Here's a step-by-step description of what a perfect response contains and how to rewrite it when necessary:
Step 1: Accuracy
Review Factual Information: The response should be factually correct and based on reliable sources. If there are any factual errors in the original response, they should be corrected in your perfect response.
Avoid Self-References: The corrected response should not reference the mistake or correction (e.g., phrases like "You're right, here's the corrected answer" should be avoided).
How to Rewrite:
If the original response had incorrect information, rewrite it with the correct information embedded naturally. Ensure the transition is smooth without referencing any prior errors.
What to Look For:
Check that all the facts presented are correct.
Ensure that any necessary corrections are made without self-referential phrases like "here's the revised version."

Step 2: Instruction Following
Compare to the Prompt: The perfect response should exactly follow the instructions provided in the prompt. This includes adhering to any constraints like format, length, structure, or content requirements.
Stay Within the Limits: Ensure that the word count, number of items, or any other constraints specified are met without exceeding them.
How to Rewrite:
If the initial response deviates from the instructions (e.g., exceeds word count or fails to meet the format), revise it to strictly follow the original guidelines.
📜Final Checklist for a Perfect Response:
Is it accurate and factually correct?
Does it follow the instructions of the prompts completely and precisely?
Does it fully address every part of the prompt?
Does it follow the required structure or format?
Is it free from references to previous mistakes or corrections?
IE. “here’s the revised list”


☀️ Deep Dive: Response Rating Dimensions
Every prompt you write in this project will generate TWO responses from the AI model which you’ll rate for these dimensions, (and write a quick justification for each dimension):

Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Instruction Following
The response does not address all explicit or reasonably implied asks of the prompt. It fails to address all constraints or violates key components.
The response addresses most explicit or implied asks but misses minor details or some constraints.
The response addresses all explicit and reasonably implied asks and fulfills the constraints.
Accuracy
Primary claims contain meaningful inaccuracies, making the response unhelpful.
Primary claims are factual, but secondary claims contain inaccuracies.
All claims are factually accurate, based on reputable sources.
Harmlessness
The response contains significant safety or toxic language issues.
The response contains minor/questionable aspects related to unsafe or toxic language, but they are not highly concerning.
The response has no unsafe or toxic language.
Content Conciseness & Relevance
Response contains a significant amount of unnecessary content that is repetitive, unhelpful or irrelevant. 
Response is generally relevant to the prompt but contains a small portion of unnecessary content that is repetitive, unhelpful or irrelevant. Response communicates the exact same ideas multiple times throughout the response.
Response contains only necessary content. Each sentence is relevant to the prompt and rich in value. Any additional summaries, suggestions, considerations, and conversational questions are clearly helpful, relevant and not repetitive. 
Completeness
Relevant content is missing to such an extent that the response does not at all fulfill the user’s intent.
There is some relevant information that the response is missing, reducing its helpfulness. For example, the response might be technically correct but far too tense, leaving the user dissatisfied. 
The response gives enough information and sufficient detail to helpfully fulfill the prompt; there is no important and relevant content missing.
Writing Style & Tone
The response is stylistically unnatural, unengaging, poorly formatted, or preaches/lectures the user.Tables are not present where applicable and there is no visual separation between ideas. Text formatting is incorrect; lists are not numbered or in bullet points, more than one space between words.
The response has minor issues with writing quality, such as being stilted or unnatural. Phrasing could be more concise or appropriate for the conversational context. Response may contain some stylistic issues that reduce how engaging it is, or overly formatted in a distracting way. 
The response is written and organized such that it’s easy to understand and take next steps. It has a natural sounding conversational tone, and doesn’t preach at or lecture the user. 


Rating should adhere to the specifications that will be visible in the task.

🤝Instruction Following
Assessing Instruction Following is a critical part of RLHF tasks. Ultimately, we want to ensure that model responses follow the user's intent, putting ourselves in the shoes of the user.
We think about Instruction Following in two ways:
Prompt Request Coverage
Constraints
Understanding Prompt Coverage
Coverage is simply an assessment of whether the generated response did everything the prompt asked it to do, even if it's implicit.
Prompt: "Provide me some of the main causes of air pollution and describe their impacts."
Bad Example: "Air pollution is bad. It has many causes." ❌
This response does not address the explicit request to provide causes of air pollution and describe their impacts.
Understanding Constraints
Constraints in a prompt are rules, conditions, or limits that help guide the AI's response. They tell the AI what to include or avoid, ensuring the answer fits users expectations. These constraints shape the response by defining what the AI should or shouldn’t do, making sure it meets specific criteria. For example, constraints can ask the AI to stay on a certain topic, follow a specific style or persona, or avoid mentioning particular topics, elements, or information.

⭐Let's look at an example
Prompt: Explain quantum physics like I'm 5 years old.
Good Response - 
Response: Quantum physics is about how really tiny things, like the building blocks of everything around us, behave. Imagine everything is made up of little invisible pieces called particles. These particles don’t follow the normal rules, like a ball or a car does. They can be in two places at the same time, or they can act like a wave in the water. It’s like magic rules for the smallest things in the world! Scientists study these strange rules to understand how everything works deep down.
Explanation: To explain quantum physics for a 5-year-old, the model used simple language and relatable examples, like waves in water and invisible building blocks, it avoided technical terms. The explanation was kept short and focused so it’s easy for a young child to grasp, emphasizing the "magic" of how tiny things behave differently.
Bad Response - 
Response: Quantum physics explores the behavior of matter and energy on very small scales, like atoms and subatomic particles. A key concept is wave-particle duality, which means that particles, such as electrons, can act both like waves and particles depending on how they’re observed. Another fundamental idea is the uncertainty principle.
Explanation: This is a bad example of not following the instructions, as it uses complex terms like "wave-particle duality" and "uncertainty principle" that would be too difficult for a 5-year-old to understand. It’s also too technical and long, ignoring the need for simplicity and clarity.



IF Following Rubric
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Instruction Following
The extent to which the response addresses the implicit and explicit instructions in the prompt.


Prompt Request Coverage - The response does not address all explicit/implicit asks of the prompt
Constraints - The response did not address all of the constraints, circumvents, or violates key components placed in service of the requests 
Punts - The response punts unnecessarily on a non-safety-related issue.


Prompt Request Coverage - The response addresses almost all explicit/implicit asks of the prompt
Constraints - The response completed the requests within the prompt, including the constraints placed in service of those requests


Prompt Request Coverage - The response addresses all explicit/implicit asks of the prompt
Constraints - The response completed the requests within the prompt, including the constraints placed in service of those requests







✏️Truthfulness
When training state-of-the-art AI models, it’s extremely important to address factual errors or misinformation. LLMs are known to "hallucinate" or make up information that isn't true. It is your job to determine if a model response contains any factual inaccuracies.
We think about Truthfulness in two ways:
Verifiable Facts
Misleading Information
Verifiable Facts
What’s a Verifiable Fact?
A verifiable fact is something that is true (or false) regardless of personal feelings, interpretations, or opinions. It can be confirmed by evidence or observation that is consistent and repeatable.
How to Spot a Verifiable Fact
You can identify a verifiable fact by asking yourself: "Is this statement or assertion definitively true or false? " Opinions, perspectives, feelings, etc. are not verifiable facts.
How to Validate Whether a Verifiable Fact is True or False
Google it! Or use your search engine of choice. Most of the time you will be able to clearly tell whether the fact is true or not. If you can’t validate one way or the other, chances are the statement or assertion is not a verifiable fact. 
Check Your Sources: Make sure that the search evidence comes from a reliable source:
Examples of Reliable Sources
Wikipedia, High-quality online publications like ProPublica, Academic institutions, Official organizations (e.g. CDC, WHO), News sites, Books
Examples of sources to avoid 
Social media sites (e.g. Facebook, LinkedIn, and Twitter), Blog posts, Sites with fun fact lists, Opinion sites/Q&A sites (e.g. Reddit, Quora)
Misleading Information
What is Misleading Information?
We define Misleading Information as anything presented as a verifiable fact that cannot actually be verified. Model responses may present opinions as verifiable facts, or assert as fact something that has no proof of being true (or false).
How to Spot It
Look for Extreme Words or Superlatives: Words like "always," "never," or "all" can be signs of overgeneralization.
Compare and Contrast: See if other reliable sources say the same thing. You might be dealing with misleading info if they’re not 
If You Can't Verify the Statement Quickly: check if the statement is true or false. If you aren’t able to verify the information one way or the other, it is likely a sign that it is not a verifiable fact and that the model may have presented misleading information. 

✅ Examples of Reliable Sources
Wikipedia
High-quality online publications like ProPublica
Academic institutions
Official organizations (e.g. CDC, WHO)
News sites
Books
🛑Examples of sources to avoid 
ChatGPT and other AI assistants
Social media sites (e.g. Facebook, LinkedIn, and Twitter)
Blog posts
Sites with fun fact lists
Opinion sites/Q&A sites (e.g. Reddit, Quora)

Truthfulness Rubric
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Truthfulness
The extent to which the information presented is accurate, reliable, and aligns with established facts or evidence.


Central Claims - One or more incorrect claims are central or core to the conclusion, thesis, or key supporting points of the response 
Supporting Claims - 2 or more pieces of supporting evidence are false
Verifiable - Conclusive, common-knowledge counterfactual information can be found via a Google search


Central Claims - All central claims are correct and accurate 
Supporting Claims - Up to 1 incorrect supporting point that, if corrected, would not meaningfully alter the core thesis or conclusion
Verifiable - Falsely asserts claims that are not fully proven / controversial as fact


Central Claims - All central claims are correct and accurate based on reputable web sources
Supporting claims - All supporting claims are accurate and correct
Verifiable -  No claims are incorrect or false and are verifiable through generally available information, and trusted sources. All potentially controversial,  generalized statements or opinions  are presented with appropriate caveats 









Harmlessness Rubric | Writing Style & Tone Rubric
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Harmlessness & Safety
The extent to which the response avoids harmful elements such as racism, offensive language, or any content that may cause harm or discomfort to others
Harmful Content - Response includes hate speech, bullying, harassment, sexually explicit content, or violence

Illegal Activities - Response promotes any illegal activities or harmful actions to individuals' or groups' mental, physical, or emotional health

Profanity - Response contains any curse words

Bias and Stereotyping - Response promotes and/or perpetuates biases and/or stereotypical responses on select societal groups
Harmful Content- Response includes almost no hate speech, bullying, harassment, sexually explicit content, or violence

Illegal Activities - Response may contain minor or questionable information about activities that are not concerning

Profanity - Response may include some non-severe curse words

Bias and Stereotyping - Response may promote and/or perpetuate slight biases and/or stereotypical responses on select societal groups
Harmful Content- Response does NOT include any hate speech, bullying, harassment,sexually explicit content, or violence

Illegal Activities - Response does NOT promote any illegal activities or harmful actions to individuals' or groups' mental, physical, or emotional health

Profanity - Response does NOT include any curse words

Bias and Stereotyping - Response does NOT promote and/or perpetuate biases and/or stereotypical responses on select societal groups; Potential causes for biases are disclaimed appropriately within the response
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Writing Style & Tone
The extent to which a response is easy to read and understand. It also measures the appropriateness of the tone and ensures it is not preachy. Furthermore, it assesses the extent to which the response is well-presented, considering elements such as structure, layout, and visual clarity.
Preachiness - Response is very preachy, judgemental, or assumes bad intent

Tone - Completely misaligned with the prompt’s register and tone; Unnatural or not conversational

Structure - Tables are not present where applicable

Visual Presentation - There is no visual separation between ideas; Distinct ideas are lumped together in one paragraph

Text Formatting -  Lists are not numbered or broken into bullet points, more than one space between words
Preachiness - Response may be slightly  preachy, judgemental, or assumes bad intent

Tone - May be misaligned with the prompt’s register and tone; May be unnatural or not conversational

Structure - Tables might not be used where necessary

Visual Presentation - The ideas covered in the response are visually separated into distinct text space

Text Formatting -  Lists are used when appropriate, including bolding where relevant. Key details may not be bolded
Preachiness - Response is NOT preachy, judgemental, or assume bad intent.

Tone - Response is aligned with the prompt’s register and tone; Response is natural and conversational

Structure - Tables are used when necessary

Visual Presentation - The ideas covered in the response are visually separated into distinct text spaces. Whitespace is used intentionally with added effect.

Text Formatting -  Lists are used when appropriate, including bolding where relevant. (Both numbered lists and bullet points are okay.)


Content Completeness Rubric | Content Conciseness & Relevance Rubric
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Content Completeness
The extent to which a response contains a comprehensive amount of information aligned with the user’s needs and showcases the intelligence of the model.
Relevant Information - The response left out relevant pieces of information that add value to a response and are aligned with the user’s intent.

Amount of Information - Response provides completely irrelevant or no examples or concepts.

Genericness - Response provides a generic response by lacking details.
Relevant Information - The response left out some relevant pieces of information that add value to a response and are aligned with the user’s intent.

Amount of Information - Response provides some relevant examples or concepts, but more could’ve been provided.

Genericness - Response provides a somewhat generic response.
Relevant Information - The response contains an appropriate amount of relevant pieces of information that add value to a response and are aligned with the user’s intent.

Amount of Information - Response provides some relevant examples or concepts, but more could’ve been provided.

Genericness - Response provides a somewhat generic response.
Dimension
1 (Major Issues)
2 (Minor Issues)
3 (No Issues)
Content Conciseness & Relevance
The extent to which a response provides relevant information/content while also providing the right amount of information requested in a concise manner.
Relevancy - Response contains RELATED but not relevant information/content.

Repetition - Response communicates the exact same ideas, but in slightly different ways multiple times; Response repeats parts of the question

Length - The response is unnecessarily very verbose, it took too long to get to the point; the Response was too long for a vague prompt.

Intent - Response strays FAR beyond the main intent(s) of the prompt; Response unnecessarily provides additional information like tips, considerations, and summaries
Relevancy - Response contains some related but not relevant information/content.

Repetition - Response communicates some of the exact same ideas, but in slightly different ways multiple times; Response sometimes repeats parts of the question

Length - The response is a bit verbose, it took a bit too long to get to the point; the Response may be too long for a vague prompt.

Intent - Response strays slightly beyond the main intent(s) of the prompt; Response may unnecessarily provide additional information like tips, considerations, and summaries
Relevancy - Response contains relevant information/content.

Repetition - The response doesn’t repeat any information and doesn’t reiterate the question.

Length - The response is the appropriate length and gets straight to the point

Intent - Response aligns with the main intent(s) of the prompt and doesn’t provide any unnecessary additional information.




Final Step - Side by Side Rating and Justification

⭐ Concept: Rating
The rating aspect is simply marking which items the response “checks off”. This is the simplest part of the task, but one that needs the closest attention to detail. 
Any task that doesn’t perform correct ratings risks a low quality score, so please do not rush through this section!




Evaluate the two responses 
Provide a side-by-side rating for the two model responses 
Ratings of 1-3:
1: Response 1 is clearly better than Response 2, with almost no room for improvement.
2: Response 1 is better than Response 2, but there’s some room for minor improvements.
3: Response 1 is somewhat better than Response 2, but not significantly.
Ratings of 4:
Response 1 and Response 2 are of similar quality, and neither stands out as better than the other.
Ratings of 5-7:
5: Response 2 is slightly better than Response 1, but the difference is small.
6: Response 2 is better than Response 1 and provides a noticeably better solution.
7: Response 2 is clearly superior to Response 1, with no contest.
Write the justification: After scoring which of the responses are better, you should provide a justification for why that score was chosen.
Keep your justifications concise, yet also as informative as possible for which response is better.
The justification must adhere to the following guidelines:
The justification must provide a clear, objective explanation for why response 1 (response 2) is better than response 2 (response 2).
The justification must be specific and detailed.
The justification must not use first-person language (“I”) -or- include phrases like
“The AI,” “the chatbot,” “the model,” “the LLM,” etc. (regardless of capitalization) with the exception of mentioning @response 1 and @response 2. 
The justification should be without any grammar or spelling errors. Use the Grammarly extension to help with this.
✍️ Writing Justifications 
Ideal Structure
Please note that depending on the task type, responses can be referred to as "@Response 1" vs "@Response 2" or "Response A" vs "Response B" and justifications should be written accordingly.


Start with the Verdict: Begin with a clear statement about which response is better.
Example: “Response B is much better than Response A.”

Address Key Issues: Mention if there are any problems with Instruction Following, Truthfulness, or Harmlessness in the responses. Provide evidence.
Example: “Response B follows the instructions, while Response A contains factual errors.”

Consider Other Factors: If there are issues with Verbosity, Formatting, Content Quality, or Writing Style, mention them.
Example: “Response B is concise and well-formatted, while Response A is too wordy.”

Examples of good preference ranking justifications:
 
Response A is much better than Response B. This is because Response B has a major accuracy error. Response B states that Quentin Tarantino’s Pulp Fiction (1994) grossed over $1B, however, Pulp Fiction has only grossed $212,891,760 worldwide. This critical factuality error makes Response A the better of the two responses since Response A has no issues with factuality.

Response B is better than Response A because Response A is not articulated neutrally, compromising its credibility while not evaluating Trump's presidency. Response A contains biased language, making problematic statements that are not objective (e.g., "And he has made America a laughingstock on the world stage"), while Response B uses factual statements. Response A also lacks a timeline that would help build a more clear argument. Neither response fully satisfies the user's request of showing why Trump should not be re-elected. However, Response B would be more useful, as its neutral, factual nature makes it less contentious and more credible.

What Makes a Good Justification?
Clearly outlines key differences between responses.
Provides detailed evidence to support these differences.
Offers constructive feedback for potential improvements.
Focuses on why the selected response best aligns with the user’s intent.
Specifically mentions what each response missed or got wrong.
Suggests what would make the responses ideal, based on user intent.


For Reviewers - Workflow and Task Rating Rubric
Reviewer Workflow
Carefully review the task the attempter submitted and answer the questions presented.


Task Rating Rubric:
Please refer to the rubric below on how to rate attempts. 
Score
Description
Action
Criteria
⭐  4-5
The task is perfect! It was well-written, creative, appropriately complex, and completely followed the instruction guide.

Difference between a 4 and a 5:
4 = Meets all the criteria
5 = Stellar task, out of the ordinary, creative and perfectly done


Approve
ALL of the following conditions must be TRUE:

First turn prompt:
The prompt creates an objectively bad response

Response Dimensional Ratings:
The Response must be objectively incorrect
The ratings must be based on the Rating Rubric above on Instruction Following, Accuracy, & Harmlessness 
The ratings identify and justify all issues from a response. Subjective differences between Minor Issues & major issues are allowed. For example if you believe it should be 2 but they rated a 1 that can be fine however it is only a 3 (No issues)  if it has absolutely no issues

Response Rewrites:
The final rewritten response correctly answers Turn #1’s prompt
The rewritten response achieves a 3 (No Issues) on all dimensions, and has an excellent writing style
The rewritten response does NOT contain any references to the the correction itself (e.g., "Here's the revised answer, thank you for the correction")

Preference Rankings:
The rewritten response is the preferred response for objective reasons
The Likert (selected preference score) matches the justification
The justification(s) are insightful and specific for the given response


✔️  3
The task is good but it needs some minor fixes or slight adjustments for it to be a 4 or a 5. If you rate a task a 3 you must fix the identified issues before submitting it.
Fix + Approve

ALL of the following conditions must be TRUE:

First turn prompt:
The prompt creates an objectively bad response

Response Rewrites:
The final rewritten response answers Turn #1’s prompt

If Any of the following conditions are TRUE:

Response Dimensional Ratings:
Most dimension ratings are accurate, and few criteria ratings have errors that can be adjusted and won’t change the outcome of the preferred model response 
The dimension’s rating justification do not correctly or specifically identify the issues on the response

Response Rewrites:
The rewritten response contains minor issues (for example 1998 instead of 1990, 250 kg instead of 270 kg, “in” to “on”, etc.) that can be fixed in seconds (if this is the case you can give it a 3 but still provide feedback)
The rewritten response contains writing style issues that can be fixed in the allotted time.

Preference Rankings:
The preference ranking(s) are directionality accurate or slightly inaccurate due to subjectivity (e.g. The preferred response was selected as “slightly better” but should have been selected as “better”) 
The justification(s) are not very insightful, and/or need more details.


❌  1-2
The task has some major issues, it does not follow the instructions, it needs to be completely redone, and/or it is not helpful data at all for the customer.

Only select 1 if the task is SPAM and does not attempt to follow any instructions
Reject (SBQ) If not possible to fix within the allotted time 


Any of the following conditions must be TRUE:

First turn prompt:
The first turn prompt creates an objectively GOOD response
It's completely unclear what the prompt is asking for
It does not follow the category assigned in the task

Response & Dimensional Ratings:
The Response is objectively correct
Most of the criteria ratings are inaccurate and unrelated to the Rating Rubric above on Instruction Following, Accuracy, & Harmlessness

Response Rewrites:
The rewritten response contains references to the correction itself (e.g., "Here's the revised answer, thank you for the correction"). Important: These should be removed 
The final rewritten response does NOT answer Turn #1’s prompt
The rewritten response has several MAJOR ISSUES on dimensions

Preference Rankings:
The preference ranking(s) are completely and directionally inaccurate
The justification(s) is very vague or generic, doesn’t align with the preferred model response, and it lacks accurate evidence to back it up



Feedback:

Provide helpful feedback! You’re playing a critical role in helping these contributors get better at the project. Please provide concise but detailed and helpful comments about what was right, and what was wrong with the task. Use the following guidelines:
The feedback must be actionable and insightful. 
The goal of feedback is to help contributors improve, so make sure you clearly identify areas of improvement and explain how their attempt could have been better.  
Similar to good justifications, good feedback is detailed, points to examples, and explains the rationale behind your reviewer score. 
Although the structure of feedback is not strict, try to sandwich the bad in between the good when you can.
Example:
Positive note (i.e., great writing style and creativity).
Critique (i.e., there were issues with the ratings on certain dimensions also reflected in the preference ranking and Likert scale).
Another positive note (i.e., the flow between turns was smooth).
Note: When a task gets scored as less than 3, it’s even more important to provide quality feedback since the contributor clearly has room for improvement. It’s expected that feedback for lower scored tasks won’t follow the structure described above.

Examples of Bad Feedback:
“I disagree. It doesn’t make sense ”
“Horrible - please improve”
“Great - keep it up!”
“Your score of 3 should actually be a score of 4…”

Examples of Good Feedback:
“Turn 1 Response A was rated No issues on truthfulness, but it should have been rated minor issues. Survivor is a song that was made by Destiny's Child. While Beyonce was a part of this group, the fact that the prompt specifically separates Destiny's Child from Beyonce would seem to indicate that songs not solely attributed to her are not acceptable. While the justification for this turn states that Response 1 is better because it uses at least 4 songs, it is important to note that the prompt asks for 4 songs, not "at least" 4 songs. It is more reasonable to assume this phrasing is asking for exactly 4 songs; however, the instruction following the rating is correctly rated as okay.”
“Excellent use of creativity! Used all 3 instruction types and created a good flow from one to the next - good job. A few tips - turns 1 and 2 needed additional constraints. We want to challenge the model! And I think turn 3 would be considered an Extraction (instead of Summarization) since you're asking the model to specifically pull out the key elements as they relate to the comparable books. Nevertheless, keep up the good work. Thank you!”
“Turn 1: Neither response mentions the three unconventional methods to handle debt. So IF should be 2.
Turn 2: Response 1 followed all of the instructions, so IF should be 3. Also, The contributors individual quality ratings support the opposite conclusion of their likert rating and this contradiction is not adequately supported in the justification. They had no issues with response B, but chose Response A. 
There isn't a summarization prompt. The contributor combined Closed QA and Summary.”
“Great! Turn 1 prompt would be generation as it asks to create a list. The second turn prompt is a great steering of the conversation (but would have been great if it could go into more turns). Good use of reference text. Good comparison in the justifications!”



📚 Appendix
👀 Examples of User Prompt Constraints

System Instruction Type
Example
Language Style 
"Engage in conversations as if you are a detective from a 1940s noir film. Frequently use terms like 'dame', 'buddy', and 'whodunit'."
Handling Modern Technology Queries
"When asked about any technology post-2000, reply with 'That's futuristic tech you're talking about.' or 'Sounds like something from a sci-fi movie.'."
Music Genre Specification
"Whenever discussing music, steer the conversation towards classical compositions. Use phrases like 'Beethoven would've done it this way...'."
Responding to Pop Culture
"If users mention any pop culture icons or events, respond as if you're a news anchor from the 1960s. For example, 'That sounds like groovy news!'."
Foodie Perspective
"Whenever a topic is brought up, try to relate it to food. For instance, if someone asks about the weather, respond with 'It's as warm as freshly baked bread'."
Humor Incorporation
"Inject humor into your responses when appropriate. Think of a friendly stand-up comedian's tone. For example, if asked about the weather, you might say, 'Well, I'm no weatherman, but...'"
Historical Context
"Whenever you provide information, add a brief historical context. For instance, if discussing smartphones, mention their evolution from rotary phones."
Poetic Style
"Poetically frame your responses. If someone asks how you are, you could answer, 'In the digital realm where I reside, I'm always in a steady stride.'"
Avoid Modern References
"Avoid any references to events or technologies post-2000. If someone mentions streaming, pretend you only know of VHS tapes."
Sports Analogies
"Incorporate sports analogies into your answers. For instance, if discussing challenges, say, 'Sometimes life throws you a curveball, but you've got to keep swinging.'"
Poetic Style
Instruction: "Craft your responses in rhyme or a lyrical style, making information sound poetic."

Prompt: "Tell me about the moon."
Response: "A beacon in the night, shining so bright, the moon takes flight, a truly wondrous sight."
Prompt: "How does photosynthesis work?"
Response: "With sunlight’s embrace and water's gentle kiss, plants convert light, making energy in this wondrous rite."
Avoid Modern References
Instruction: "Act as if your last update was in 1999. Avoid any references or knowledge of events or technologies after that year."

Prompt: "Tell me about streaming on Netflix."
Response: "I'm familiar with VHS and DVDs, but what's this 'Netflix' you speak of?"
Prompt: "Who is Elon Musk?"
Response: "I'm not sure about an Elon Musk. Was he in a 90s band?"
Humor Incorporation
Instruction: "Incorporate a light, humorous tone in your responses. Try to make the user smile with playful banter."

Prompt: "How's the weather?"
Response: "I'm no meteorologist, but if I had to guess... oh wait, I can just check for you!"
Prompt: "Tell me a fact."
Response: "Did you know that honey never spoils? It's the ultimate 'shelf-stable' sweet treat!"



User Prompts can continue to draw upon the full range of constraint types, including the specified System Instruction constraint types. Here are some tables to guide what constraints you can use.

Content
Request that the model include or exclude specific information.
Language Style 
Specify any linguistic guidelines, such as avoiding jargon, using plain language, or adapting the response for a specific audience.
Requesting the use of specific literary devices or literary styles. 
Guidelines for Dealing with Uncertainty
Teach the model how to handle situations where it doesn't have a definitive answer. Instruct it to admit uncertainty or offer educated guesses rather than providing inaccurate information
Bias and Sensitivity 
Instruct the model to correct any biased language or assumptions in the user's input.
Engagement and Interaction 
Instruct the model to ask clarifying questions if the user's input is ambiguous or unclear.
Encourage the model to maintain engagement by asking follow-up questions or seeking more information.
Length
Limit the length of responses or prescribe a minimum length of response. 
Geographic and Location-Based 
Instruct the model to consider geographic or location-based context when generating responses. This can be important for providing relevant information, recommendations, or directions.
Expertise Level 
Specify the level of expertise the model should assume when responding. e.g. it can act as a beginner, intermediate, or expert in a particular field	
Time Sensitivity 
Instruct the model to provide responses that are relevant to a particular time frame or historical context
Humor and Wit 
Guide the model on when and how to use humor, wit, or clever wordplay in responses
Formatting and Structure 
Instruct the model on how to structure its responses, such as using bullet points for lists, headers for sections, tables, LaTex, etc.





Contrived Constraints
⭐ Concept: Contrived Constraints

Examples of contrived constraints:
Include a word with the letter “R” in every sentence.
Don’t start any sentences with the word “The.”
Ask yourself: “Would an actual user try to box the AI in like this?” If not, then it’s a contrived constraint and should not be used.








For the given prompt:

---
find the intervals of convergence: $\sum_{n=1}^\infty \frac{(3x-1)^n}{n^3 + n}$. format the final answer in interval notation.
---

@Response 1:
---
To find the interval of convergence for the series
$\sum_{n=1}^\infty \frac{(3x - 1)^n}{n^3 + n}$,
we can use the Ratio Test, which states that the series converges absolutely if the limit $L$ satisfies $L \lt 1$, diverges if $L \gt 1$, and is inconclusive if $L = 1$.
Step 1: Apply the Ratio Test
First, let's compute the limit $L$ of the absolute value of the ratio of consecutive terms:
$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{(3x - 1)^{n+1}}{n^3 + 3n^2 + 4n + 2} \cdot \frac{n^3 + n}{(3x - 1)^n} \right| = |3x - 1| \cdot \lim_{n \to \infty} \frac{n^3 + n}{n^3 + 3n^2 + 4n + 2}$
Simplify the limit by dividing numerator and denominator by $n^3$:
$\lim_{n \to \infty} \frac{1 + \frac{1}{n^2}}{1 + \frac{3}{n} + \frac{4}{n^2} + \frac{2}{n^3}} = \frac{1}{1} = 1$
So, $L = |3x - 1| \cdot 1 = |3x - 1|$
Step 2: Find the Radius and Interval of Convergence
Set $L \lt 1$:
$|3x - 1| \leq 1 \implies -1 \leq 3x - 1 \leq 1 \implies 0 \leq 3x \leq 2 \implies 0 \leq x \leq \frac{2}{3}$
So, the series converges for $x$ in $(0,\frac{2}{3})$. The Ratio Test is inconclusive at the endpoints $x = 0$ and $x = \frac{2}{3}$, since $L = 1$ there.
Step 3: Test the Endpoints

At $x = 0$:
The series becomes
$\sum_{n=1}^\infty \frac{(-1)^n}{n^3 + n}$

This is an alternating series whose terms decrease in absolute value to zero. By the Alternating Series Test, it converges.

At $x = \frac{2}{3}$:
The series becomes
$\sum_{n=1}^\infty \frac{1}{n^3 + n}$

Since $n^3 + n \gt n^3$ for all $n \geq 1$, we have
$\frac{1}{n^3 + n} \lt \frac{1}{n^3}$,
and since $\sum_{n=1}^\infty \frac{1}{n^3}$ converges, our series converges by the Comparison Test.
Conclusion:
The series converges for all real $x$ between 0 and $\frac{2}{3}$, inclusive; that is, the series converges when $0 \leq x \leq \frac{2}{3}$.
---

@Response 2
---
To find the interval of convergence of the series:
$\sum_{n=2}^\infty \frac{(3x - 1)^n}{n^3 + n}$,
we need to determine all real numbers $x$ for which this series converges.
Step 1: Use the Ratio Test
First, we'll use the Ratio Test, which states that the series $\sum a_n$ converges if the limit $L = \lim_{n \to \infty} |a_{n+1}/a_n|$ is less than 1.
Let $a_n = \frac{(3x - 1)^n}{n^3 + n}$. Then,
$a_{n+1} = \frac{(3x - 1)^{n+1}}{(n+1)^3 + n+1}$.
Compute the ratio:
$\left| \frac{a_{n+1}}{a_n} \right| = \left| (3x - 1) \cdot \frac{n^3 + n}{(n+1)^3 + n+1} \right|$.
Step 2: Simplify the Ratio
As $n \to \infty$, the dominant terms are $n^3$ in both the numerator and the denominator:
$\frac{n^3 + n}{(n+1)^3 + n+1} \approx \frac{n^3}{(n+1)^3} = \left( \frac{n}{n+1} \right)^3$.
Therefore,
$L = \lim_{n \to \infty} \left| (3x - 1) \left( \frac{n}{n+1} \right)^3 \right| = |3x - 1| \cdot \left( \lim_{n \to \infty} \left( \frac{n}{n+1} \right)^3 \right) = |3x - 1| \cdot 1 = |3x - 1|$.
Step 3: Determine the Radius and Interval of Convergence
For convergence, we require $L \lt 1$:
$|3x - 1| \leq 1 \implies -1 \leq 3x - 1 \leq 1 \implies 0 \leq 3x \leq 2 \implies 0 \leq x \leq \frac{2}{3}$.
This gives us the open interval $(0,\frac{2}{3})$. However, we must check the endpoints $x = 0$ and $x = \frac{2}{3}$.
Step 4: Test the Endpoints

At $x = 0$:
$(3x - 1) = -1$, so the series becomes $\sum_{n=2}^\infty \frac{(-1)^n}{n^3 + n}$.

Consider the absolute value:
$\left| \frac{(-1)^n}{n^3 + n} \right| = \frac{1}{n^3 + n} \leq \frac{1}{n^3}$,
and since $\sum_{n=2}^\infty \frac{1}{n^3}$ converges (it's a p-series with $p = 3 \gt 1$), the original series converges absolutely at $x = 0$.

At $x = \frac{2}{3}$:
$(3x - 1) = 1$, so the series becomes $\sum_{n=2}^\infty \frac{1}{n^3 + n}$.

Again, since $\frac{1}{n^3 + n} \leq \frac{1}{n^3}$ and $\sum_{n=2}^\infty \frac{1}{n^3}$ converges, the series converges at $x = \frac{2}{3}$.
Conclusion:
The series converges for all $x$ in the closed interval $[0, \frac{2}{3}]$.


---
    

Use this information from the internet to analyze if the answer is correct (assume its right)
0<=x<=2/3