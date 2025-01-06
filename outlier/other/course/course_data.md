Goal of this project
Welcome to the Cabbage Patch Long Context Task onboarding. This lesson will guide you through the steps required to complete this task and the key skills you’ll need, including:

Writing rubrics.
Grading AI responses.
Refining your work to achieve better results.
The Cabbage Patch Long Context Task is a project designed to help AI models perform better by using rubrics and long context documents.



A rubric is essentially a checklist, outlining the steps required to generate a perfect response to a prompt. Long context documents, as the name suggests, are large texts like research papers, books, or transcripts that the AI will draw upon to answer questions.

What this course will cover
In this course, we’ll break down how to create these rubrics and evaluate AI responses. This will help you contribute to improving the accuracy of AI outputs, ensuring responses are relevant and meet all required guidelines.



Learning Objectives Recap:

You’ll know how to complete a task from start to finish.
You’ll understand the difference between instructions and constraints.
You’ll be confident in grading responses and improving your rubric.

Cabbage Patch Long Context Tasking Handbook

Last Updated: Dec 12, 2024



Updates of This Week (11/25/2024)

Project Overview

Important Documents and Resources

Task Workflow

Deep Dive: Writing a Rubric

Step 1: Make sure your prompt is focused enough

Step 2: Break each prompt ask into a criteria item

Step 3: Add in your hows

Step 4: Combine your whats and hows

Reviewer Workflow

Task Rating Rubric

Linters

Appendix

Constraints

FAQs

Reference Texts

Prompt Modifications

Rubric

Task Overall

Communication




Updates:
12/12 - Task is multiturn and multidoc now
11/26 - [FAQs] New FAQs updated
11/26 - [REF TEXT] Can I count footnotes in the token count?
Yes, as long as the footnotes are relevant to the text and prompt. Note: The footnotes/reference should account for <20% of the text.
11/25 - [LINTER] Low Quality Rubric
11/22 - [RESOURCE] How to write a prompt 
Please give this a read before starting your rubric. A bad prompt will be automatically rejected.


Project Overview
In this project, your task is to work with a lengthy document. You will refine a generated prompt related to the document, create a rubric that defines the criteria for an ideal response, and evaluate how well two generated responses meet the rubric's standards. By participating, you will help train models to accurately interpret reference texts and respond effectively to real-world prompts.


Important Documents and Resources
Full Examples w/Feedback
Common Errors
How to Fix a Prompt
Task Buddy
Where to Find Reference Texts
[VIDEO] Attempting - Start to Finish
[VIDEO] How to: Adjusting Prompts
[VIDEO] How to: Writing a Strong Rubric
Anonymized Feedback: Examples of Prompt, Rubric, and Associated Feedback



Task Workflow

Find 2 Long Context Documents. You will be providing your own reference texts, and these must be about the same topic. You can find some suggestions here. The reference texts must be:
At least 8,000 tokens long each (check here) – Note: Please avoid submitting extremely long reference texts (over 20k tokens long).
Publicly accessible: There should be no subscriptions, special logins, or any hoops to jump to access the material. Google Docs or any file in personal Google Drive are not allowed.
Copy-pasteable! You will need to copy over the text into a box, so ensure that your PDF is scannable.
One of these context types:
Books: fiction, non-fiction, …
Transcripts: video transcripts, screenplays
Research papers: nature, arXiv, pubmed, etc
Government documents: budgets, hearings, regulations, …
Financial / Business reports: equity analysis, financial statements, …
Journalism: column articles, editorial, news, …
Legal documents: tax, licenses, contracts, insurance policies, …
Reference material: user manuals, guidelines, catalogs, …

Note: The two reference texts must be used cohesively in both prompt creation and response evaluation. Rubrics and follow-up prompts should incorporate elements from both texts to ensure comprehensive coverage.


🚨IMPORTANT: You must include TWO UNIQUE DOCUMENTS. Pasting the same document twice or omitting a second document will result in an immediate failed task. 🚨




Copy over your reference texts. In the box, paste in your reference texts. In the URL box, paste in your reference link for both of the texts.




Familiarize yourself with the Prompt Type. This project has 4 prompt types. Your submitted prompt must match the prompt type requested in the task. The types are as follows:
Closed Q&A: Questions that can be answered using the reference text. For example, say our reference text is a story about Sally and Joe’s love by Author B.
✅ Good Prompt Fit: What happened between Sally and Joe in the story?
❌ Bad Prompt Fit: Tell me about Author B’s background and influence in the literary sphere.  → We wouldn’t find this information in the reference text itself.
Extraction: Identify key entities from a piece of text.
Summarization: Condense a longer text into its essential points, focusing on key ideas and information.
Rewriting: Rewrite the original text while maintaining the original meaning.

Select and modify the prompt. Several prompts will be generated based on your uploaded text. Select one. You should check and modify that each prompt:
Is the correct prompt type 
Has background context: Who is the user and/or what is the use case?
Has a clear ask: What should the response do?
Has 3 constraints (strongly encouraged but not mandatory): See here. The prompt should be focused enough that there is clear idea of what the perfect response looks like. There should not be an infinite amount of perfect responses.
Either breaks the model AND produces a significant variation:
Breaking the model means that the generated model responses have a critical error such as an inaccurate answer.
Producing a significant variation means that the content between the two responses is significantly different such that you could rate one response bad and the other response okay or good.
Sounds natural: The prompt should be something that an actual person would write or use.

                 🔗 If you’d like a deeper dive, check out this resource here!


Select the best response. You should see two generated responses. Select the best one at a skim. Don’t spend too much time on this. We’ll be coming back to it to check!

Write your rubric! Your rubric should:
Include all the asks mentioned in the prompt. This means that almost every sentence, except the background context and fluff, should be a criteria item.
Include hows. Flesh out what the response would look like if that criteria item was executed. Details here.
Be accurate. Only add criteria items that are asked for and the hows that you include are comprehensive and correctly slotted.
Group like items together. If multiple items fall into the same category such as character names, you should create 1 criteria item that lists all the character names. Do not create separate criteria items for each character name.
Classify the item:
Objective: You can answer yes/no this item is either in the response or it is not.
Subjective: There is room for interpretation of whether this rubric item is done appropriately, but a large majority (75%) of the population would agree.
Formatting: A format or presentation requirement.

Evaluate the responses against this rubric. Evaluate whether the response has no issues, minor issues, or major issues for each criteria item.
No issues: The entire criteria item is met.
Minor issues: The majority of the criteria item is met (⅖ - ⅗ pieces are included in a 5-part criteria item).
Major issues: The majority or all of the criteria item is not met (⅘- 5/5 pieces are missed). Anything >50% of the criteria is considered major.

Justify each response’s evaluation. For every criteria item where there was a minor or major issue, what was the minor/major issue? Be specific but concise.

Justify the best response. Explain which response was better and why.

Select the best response. Go back to the previous section to select the best response based on your justification. It’s okay if this changed from your original answer!
Repeat steps 4-10. This is a multi-turn task. You must ask a follow-up question that is related to the previous question. A couple of notes:
Modify the second generated prompt. Make sure your prompt meets the requirements:
Sound natural. Make sure the prompt begins as a continuation of the last turn.
Be complex - ensure that your prompt has 3 constraints
It breaks the model AND produces significant variation
Breaking the model means that the generated model responses have a critical error such as an inaccurate answer.
Producing a significant variation means that the content between the two responses is significantly different.
The prompt type for your follow-up questions can be any of the types of your choice.
The prompt still has to have 3 constraints (strongly encouraged but not mandatory) and produce response diversity.
Your rubric should only be specific to this turn’s prompt. You can exclude information based on the previous turn.

Review your task.
Make sure your entire rubric is accurate. It should be comprehensive and there should be no false claims in the rubric.
Make sure your justification matches the best response selected in the earlier section.
Make sure your evaluation is complete and accurate.

Submit!


Deep Dive: Writing a Rubric

A rubric is a checklist that outlines the key elements of an ideal response to a given prompt. It is composed of a what (from the prompt) and a how (typically from the reference text). In theory, if the same prompt and rubric were provided to a model, the responses might not be identical, but they would all be considered a perfect or 5-star response.


Let’s dive into how to write a rubric!


—

Step 1: Make sure your prompt is focused enough
🔖 Resource: How to Fix a Prompt


A strong rubric depends on a well-focused prompt. While broad prompts can lead to a variety of excellent responses, a more focused prompt narrows the possibilities, typically resulting in only 1-2 truly outstanding responses.


You can make your prompt more focused by adding constraints! Limit what you are asking to a more specific use case and the perfect response will follow.



Bad Prompt

Improved Prompt

 “Name a type of animal that would make a good pet.”

"I would like the name of at least one animal that would make a good domestic pet. Exclude any animal that can't be tamed or might be venomous. Any animal you name must be no more than 30 pounds and have a lifespan of at least 8 years. The animal has to be legal to own in the State of Pennsylvania. Your output should be in the format of "(Animal name, plural) make good pets."


Step 2: Break each prompt ask into a criteria item
To make sure that our rubric is comprehensive of our prompt, let’s use our prompt as a starting point! Note: The prompt is simplified to be used as an example. Make sure yours includes 3+ constraints.


Reference Text

Pinocchio

http://www.bigandsmallpublishing.com/uploads/2/5/0/7/25072108/23_pinocchio_world_classics_be.pdf 


Given Prompt

I’m teaching a literary analysis unit to my middle school students and want to share a sample essay with them. Could you write a concise analysis on the theme of transformation in Pinocchio? The essay should highlight three key transformations Pinocchio undergoes—physical, emotional, and moral—and explain how each is influenced by a different supporting character. Additionally, it should include a comparison to a real-world moral or philosophical concept, making it accessible and easy for middle schoolers to understand.


We want our rubric to include any item that isn’t fluff or background context. Let’s split our prompt into criteria items. You can copy-paste this directly into the criteria boxes!


Scratch Rubric


Write a concise analysis on the theme of transformation in Pinnochio
Essay should highlight three key transformations Pinocchio undergoes—physical, emotional, and moral
Explain how each is influenced by a different supporting character
include a comparison to a real-world moral or philosophical concept
making it accessible and easy for middle schoolers to understand.

Step 3: Add in your hows
A how illustrates for the model how the answer should look like. It should be as specific as possible without overlimiting the response.


Typically, you can craft the hows by:

Pulling evidence or answers from the reference text itself.
Pulling a universally agreed upon answer from a reputable resource.
Having an explicit enough rubric item to not need a how.

Let’s see examples of each case.


Case

Example

Pulling evidence from the reference text

The response needs to list all of the key figures: Adolf Hitler, Benito Mussolini, Winston Churchill, Franklin D. Roosevelt, Joseph Stalin, Hideki Tojo, Dwight D. Eisenhower, and Douglas MacArthur.

Pulling a universally agreed-upon answer

To format as an email, the response needs to have a subject line, greeting, body, closing, and signature.

Having an explicit enough rubric item

It needs to be written in Spanish.


Let’s build out the hows of our Scratch Rubric!


What

How

Explanation

Write a concise analysis on the theme of transformation in Pinnochio

❌Needs to be between 200-250 words


✅only including necessary information such as the key transformations, how each is influenced by supporting characters, and a comparison to a real-world concept.

We do not want to explain “concise” as a specific word count since it’s not specified in the prompt and it’s valid for other word count ranges to be considered as concise depending on the situation. Instead, we can describe it as only including necessary information and specifying what that information might be.

Essay should highlight three key transformations Pinocchio undergoes—physical, emotional, and moral

❌physical: becoming a living puppet, emotional: overcoming fear, moral: learning the value of honesty


✅One from this list of physical transformations: becoming a living puppet from a lifeless one, turning into a donkey for being disobedient, turning from a donkey to a boy as a chance for redemption, or becoming a real boy from a wooden puppet after showing his growth.

Another from this list of emotional transformations: selfishness to compassion where he prioritizes others such as Gepetto over his own desires, overcoming fear by facing his problems rather than running away, developing trust by leaning on people who help him such as the Blue Fairy, or from naivety to awareness where he stops being manipulated by characters like the Fox and the Cat.

Finally, one from this list of moral transformations: learning the value of honesty from his nose growing, taking on responsibility when he helps Gepetto escape the whale, disobedience to obedience by respecting Gepetto’s asks, or understanding sacrifice where he prioritizes Gepetto’s safety over his own wants.

The criteria item should be comprehensive of any applicable answers. As long as there is not an infinite list of answers, then you should provide the full list of possibilities.


Note: We are paraphrasing the items rather than providing specific quotes. This should be the case unless the prompt is asking for specific quotes to be extracted.

Explain how each is influenced by a different supporting character

❌including Gepetto, The Fox and the Cat, The Blue Fairy, The Talking Cricket, The Whale, The Coachman, The Lampwick


✅pairing the transformation to the person. Gepetto is associated with becoming a living puppet, becoming a real boy, Pinnochio transforming from being selfish to compassionate, when Pinnochio takes responsibility inside the whale, and when Pinnochio learns sacrifice. The Blue Fairy is associated with turning Pinnochio back to puppet form, his transformation into a real boy, when he develops trust, disobedience to obedience, and Pinnochio learning sacrifice. The Cricket is responsible for Pinnochio overcoming fear, learning the value of honesty. The Fox and the Cat is responsible for Pinnochio turning into a donkey and how he grows out of being naive. Finally, the Lampwick is associated with Pinnochio becoming a donkey.

We want to teach the model by giving a clear idea of what character is associated with what change. Be detailed when possible.

include a comparison to a real-world moral or philosophical concept

✅mentioning one of the following: honesty and integrity, accountability, compassion and empathy, sacrifice, virtue ethics, free will and consequences, the nature of humanity, growth through adversity, the importance of hard work, and the hero’s journey.

Since this criteria item is more open to interpretation, we can include a more general list of concepts most people could find within the text.


Ideally, we would have wanted our prompt to be more specific or constrained so we could provide a better answer.

making it accessible and easy for middle schoolers to understand.

❌use slang like “omg” and “suhhh” and keep the analysis to five paragraphs.


✅avoid jargon, define more complex vocabulary, use short sentences, and, when applicable, use references that are relatable to a middle school audience.

We should not assume that certain words or set limitations make it approachable for a specific audience. Instead, we should generally capture what makes material accessible and appropriate for a middle school audience.


🚨 Pay attention to the grouping here. We want to group like items together. Just because it’s in the same sentence does not mean they are like items.


Step 4: Combine your whats and hows
Your final rubric should be a simple combination of your whats and hows. Make sure to make any adjustments so each item is grammatically correct.


Combine Rubric


Write a concise analysis on the theme of transformation in Pinnochio only including necessary information such as the key transformations, how each is influenced by supporting characters, and a comparison to a real-world concept.

Essay should highlight three key transformations Pinocchio undergoes—physical, emotional, and moral One from this list of physical transformations: becoming a living puppet from a lifeless one, turning into a donkey for being disobedient, turning from a donkey to a boy as a chance for redemption, or becoming a real boy from a wooden puppet after showing his growth.
Another from this list of emotional transformations: selfishness to compassion where he prioritizes others such as Gepetto over his own desires, overcoming fear by facing his problems rather than running away, developing trust by leaning on people who help him such as the Blue Fairy, or from naivety to awareness where he stops being manipulated by characters like the Fox and the Cat.

Finally, one from this list of moral transformations: learning the value of honesty from his nose growing, taking on responsibility when he helps Gepetto escape the whale, disobedience to obedience by respecting Gepetto’s asks, or understanding sacrifice where he prioritizes Gepetto’s safety over his own wants.


Explain how each is influenced by a different supporting character pairing the transformation to the person. Gepetto is associated with becoming a living puppet, becoming a real boy, Pinnochio transforming from being selfish to compassionate, when Pinnochio takes responsibility inside the whale, and when Pinnochio learns sacrifice. The Blue Fairy is associated with turning Pinnochio back to puppet form, his transformation into a real boy, when he develops trust, disobedience to obedience, and Pinnochio learning sacrifice. The Cricket is responsible for Pinnochio overcoming fear, learning the value of honesty. The Fox and the Cat is responsible for Pinnochio turning into a donkey and how he grows out of being naive. Finally, the Lampwick is associated with Pinnochio becoming a donkey.

include a comparison to a real-world moral or philosophical concept mentioning one of the following: honesty and integrity, accountability, compassion and empathy, sacrifice, virtue ethics, free will and consequences, the nature of humanity, growth through adversity, the importance of hard work, and the hero’s journey.

making it accessible and easy for middle schoolers to understand avoid jargon, define more complex vocabulary, use short sentences, and, when applicable, use references that are relatable to a middle school audience.

Final Rubric - Adjustments to make grammatically correct


1. Write a concise analysis on the theme of transformation in *Pinocchio*. The essay should focus only on the key transformations Pinocchio undergoes, how each is influenced by supporting characters, and include a comparison to a real-world moral or philosophical concept.  


2. Highlight three specific transformations Pinocchio experiences: one physical, one emotional, and one moral. For the physical transformation, choose one of the following: becoming a living puppet from a lifeless one, turning into a donkey due to disobedience, turning from a donkey back into a puppet as a chance for redemption, or becoming a real boy from a wooden puppet after demonstrating growth. For the emotional transformation, select from these options: selfishness to compassion, where Pinocchio prioritizes others like Geppetto over his own desires; overcoming fear by facing challenges instead of running away; developing trust by leaning on helpers like the Blue Fairy; or transitioning from naivety to awareness by learning not to be manipulated by characters like the Fox and the Cat. For the moral transformation, choose one of these: learning the value of honesty when his nose grows as a consequence of lying, taking responsibility when he helps Geppetto escape the whale, changing from disobedience to obedience by respecting Geppetto’s requests, or understanding sacrifice by prioritizing Geppetto’s safety over his own wants.  


3. Explain how each transformation is influenced by a different supporting character. Pair each transformation with the relevant character’s role in it. Geppetto is associated with Pinocchio becoming a living puppet, becoming a real boy, transforming from selfishness to compassion, taking responsibility to save Geppetto in the whale, and learning the value of sacrifice. The Blue Fairy is linked to Pinocchio turning back to puppet form, becoming a real boy, developing trust, moving from disobedience to obedience, and learning about sacrifice. The Cricket is responsible for helping Pinocchio overcome fear and understand honesty. The Fox and the Cat cause Pinocchio to turn into a donkey and help him grow out of being naive. Lastly, Lampwick is specifically tied to Pinocchio’s transformation into a donkey.  


4. Include a comparison to a real-world moral or philosophical concept, selecting one of the following: honesty and integrity, accountability, compassion and empathy, sacrifice, virtue ethics, free will and consequences, the nature of humanity, growth through adversity, the importance of hard work, or the hero’s journey.  


5. Make the analysis accessible and easy for middle schoolers to understand. Avoid using jargon, define complex vocabulary clearly, use short sentences, and incorporate relatable examples when applicable to connect with their experiences.




Reviewer Workflow
Carefully review the task the attempter submitted and answer the questions presented.

Use your checklist when providing your reviews to ensure you don’t miss anything!

[DRAFT] Cabbage Patch Long Context Reviewer Cheat Sheet


⚠️Remember we are fixing as much as possible!

Task Rating Rubric
Please refer to the rubric below on how to rate attempts.

Score

Description

Action

Criteria

⭐  4-5

The task is perfect! The rubric was well written, the prompt was complex and all checklists were correctly made



Difference between a 4 and a 5:

4 = Meets all the criteria

5 = Stellar task, out of the ordinary, creative and perfectly done


Approve

ALL of the following conditions must be TRUE:

Prompt:

The prompt is inline with the category assigned
The prompt is complex and challenges the model
Rubric:

Covers the core instructions
Covers all the constraints
Criteria are objective and specific
All the prompt asks are covered in the criteria
Criteria from the same prompt ask is grouped into single criterion
Rubric provides only necessary information
Criteria provide the “how”
Criteria do not add things not required for an ideal response
Each criteria covers one topic
The justification is insightful
Response Checklist:

When all the information from the criterion is covered the criterion is marked as having No Issues
When most of the information (ie 2/5 topics) are covers the criterion is marked as having Minor Issues
When the information from the criterion is not covered at all in the response, the criterion is marked as Major Issues
✔️  3

The task is good but it needs some minor fixes or slight adjustments for it to be a 4 or a 5. If you rate a task a 3 you must fix the identified issues before submitting it.

Fix + Approve


ALL of the following conditions must be TRUE:


Prompt:

Prompt is in the given category
Prompt is complex and challenges the model

Rubric:

Rubric provides the necessary information for a perfect response
Rubric provides a good base for a perfect response

If Any of the following conditions are TRUE:


Rubric

Most of the criteria required for a perfect response are present, but some fixes are needed to ensure the rubric follows the guidelines
A few criteria miss the “How”
or

A few criteria need to be grouped

Response Evaluations:

Most criteria checklists are correct, but 3 or less need to be fixed
❌  1-2

The task has some major issues, it does not follow the instructions, it needs to be completely redone, and/or it is not helpful data at all for the customer.


Only select 1 if the task is SPAM and does not attempt to follow any instructions

Fix and only Reject If not possible to fix within the allotted time


Any of the following conditions must be TRUE:


Prompt:

The prompt does not match the category
The prompt is not complex and asks for basic information
Rubric

The rubric is missing more than half of the criteria needed
The rubric provides examples
The rubric contains unnecessary information
The rubric provides vague criteria
The rubric has criteria that are not objective
The rubric does not provide the how
The rubric separates criteria for one specific prompt ask
The rubric provides inaccurate criteria

Response Evaluation:

The response evaluations have more than 3 incorrect checks


Linters
Below is a list of linters you may encounter, what they mean, and how to tackle them!



Linter Name

Explanation

How to Fix

Do Not Use Examples

Your rubric item(s) might be using specific quotes or a limited range of examples.


Note: This is often seen when your rubric matches a single generated “perfect” response rather than a range of perfect responses.

Paraphrase your hows into more general umbrellas.


See Step 3 in Deep Dive!

Reference Document Too Short

Your selected text is <8k tokens.

Pick a new reference text.


See Reference Text

Non best response was selected

Your justification listed one response as the best, but in the earlier section, you selected a different response.

Check that your justification and selected best response is the same.

Prompt Input - Require only 1 attachment of 1 reference

You added more than one reference text.

Add only the one you want to use.

Rubric criteria satisfy requirements

Your rubric looks like it is missing direct asks from the prompt.

Check the following:

1. The rubric covers the core instruction in the prompt


2. The rubric is objective and can be answered with True or False.


3. The rubric is specific, relevant, and uses the same language as the prompt.


4. Every item on the rubric is essential for a perfect response. Removing any item would mean the response is incomplete.

Prompt Type Enforcer

Your submitted prompt does not seem to match the prompt type asked for in the task.

Check that your prompt matches the prompt type!


See Step 3 in the Task Workflow!

[NEW] Low Quality Rubric

Your submitted rubric seems too simple.

You should make sure that you’ve covered all the asks from the prompt and hows for each item.


See Step 4  in the Deep Dive: Rubrics



Appendix

Constraints

Type

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


User Prompts can continue to draw upon the full range of constraint types. Here are some tables to guide what constraints you can use.


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
FAQs
Reference Texts
Can I count footnotes in the token count?
Yes, as long as the footnotes are relevant to the text and prompt. Note: The footnotes/reference should account for <20% of the text.

Can I use NYT articles or the like?
No, this is subscription-based.

Can I use Wikipedia?
Yes. It must meet the token count.

My token counters give me different token counts.
This counter should be your source of truth.

Can I use PDFs from science publications?
Yes, as long as it is not excessively long, meets the token count, and you can copy-paste the text.

Can I use non-English texts?
No.

Can I reuse a text?
You may reuse a given reference text up to 2 times.

If I want to use just a section of the Reference Document for my task, can I just paste that section in the Reference Text box?
No, you have to paste the whole reference text in the box, whether it's being used completely or not.
Prompt Modifications
What is a strong vs weak constraint?
A strong constraint forces the model to showcase some logic or thinking whereas a weak one does not.
Some examples of weak constraints include: format in a bulleted list, add bolding to the heading, include “How are you” at the beginning of the response, etc.
Some examples of strong constraints include: when mentioning a supporting character, provide additional details on how their actions develop the main character, write from the perspective of the villain, only include examples that are relevant to people in the 15th century.

If I am given a prompt type, but have a prompt that includes that prompt type and another, is that okay? (Ex: Prompt type - Extraction, Prompt - Extract the key characters and summarize chapter 2)
Yes, as long as the prompt type is met in some manner, it counts!

If my prompt falls between two prompt types, does this count as meeting the prompt type?
Depends. Evaluate how much you are stretching the prompt to meet the prompt type. If it’s a debate, make the prompt more aligned with the prompt type.

Can I ask for the response in a language other than English?
No.

I was told that we no longer had the 3+ constraint in the prompt. Is this true?
It’s not a strict requirement, but it serves as strong guidance. If you can break the model or create significant variation while also developing a well-detailed rubric, that’s perfectly acceptable! The goal is to use it as a helpful tool for creating robust prompts and rubrics.
Rubric
Does my rubric need to use the format: The response must/should ______?
Nope! As of 11/15/2024, you can use alternative formats. It should still be clear what is required to be in the response.

What is the minimum number of items I should include in the rubric?
There is no minimum requirement, but typically a decent rubric has at least 3.

Is my rubric specific enough?
Take a look at some examples!

How must the rubric be done? Do we have to give Examples or specific info?
The rubric for Closed QA and Extractions must have the textual, explicit information from the reference document to include in the Response.
The rubric for Rewriting and Summarization must not have the textual information to include in the Response, meaning, it shouldn't have the exact rewrite or summary, but must have all the specific information to include in the summary, more like a guidance, but with the information as detailed as needed for a perfect rewrite/summary to be executed.
The rubric must follow the "The response must/should (or any analogous words) ______ by including the following (or any similar expression) _____" stating the what as literal as possible from the prompt and the hows as discussed above.

What does it mean to be using examples?
It means that when you include evidence in the how part of your rubric, you do not include all possible variations. Instead, your rubric only encompasses 1 perfect response when there are others.
For instance, if the prompt was “Give me 2 suggestions of dog names for golden retrievers” and you put “The response must be Lucky and Justin.” This is only 1 correct answer, but we could have chosen other pairs too.

How do I know when to group things in the rubric or break them in several criteria?
For format requests: All format requests (bolding, italics, bullet lists, number lists, underlines, crossed text, word count, etc.) can be grouped if they don't relate to specific response parts, meaning, they pertain to sections or the whole response.
If the prompt asks to structure the response in different sections and indicates or implies section naming, this should be in its own criterion.
All content requests that share a common what (the action for the model to do) in one sentence must be in one criterion, it doesn't matter if it applies to different information in the reference text. E.g, asking to explain x, y and z, all x, y and z explanations along with the what should be in the same criterion.
Here is an example of how to write the rubric both in grouping and redaction (see prompt screenshot attached):
C1. The response must summarize the key ideas that discuss mental and physical presentations of Polycystic Ovary Syndrome (PCOS) in women during
their reproductive years by displaying all or most of the following: (here you add each "key idea" for the specific focus, all possibilities should be shown)
C2. The summary must include a brief definition and history of PCOS by showing the following in an initial paragraph: (here the definition given and history is explicitly stated, only this)
C3. The definition/history paragraph must include important dates that mention PCOS first name (Stein-Leventhal syndrome) by including the following: (here dates are added)
C4. The summary must include how PCOS got its first name by including the following: (here the explanation is included).
C5. The summary must have three paragraphs with a bolded title for each one and must be 500 words.
Do we mark down a response if it contains inaccurate info but that piece of info isn't part of any criteria? For example, if the ref text only has two characters: character A and character B. Then a criterion says 'The response must extract all characters in the text by mentioning character A and character B'. However, the model response included not only A & B but also made up a fake character C. In this case, the criterion is fully satisfied because the response included all the 'how' (A & B) but the model response added a non-existent character C. How do we rate this criterion? It makes sense to rate it 'no issues' but the model response contains some inaccurate info so it feels weird to rate the response a 5.
In case a response contains inaccurate info that wasn’t part of the criteria, the correct procedure is to add in a criteria about accuracy in the rubric & mark the error.

Task Overall
I was assigned a task that isn't mine, should I skip it?
Not necessarily, if the Reference Document is good in token count and you feel comfortable working with it and with the task overall, you can complete the task.
If you don't, skip it.

As a reviewer, if the prompt is asking for something not in the reference doc, should I mark it?
If it is a common knowledge request, such as definitions or news, and it is objectively defined, keep working with it, but highlight it in your Feedback section.
If the request requires another document/article/specific website in order to fulfill the request that is not the reference document, remove the request/modify it and mark it in your Feedback.

How much time do I have for tasking? how much for reviewing?
Current time limits are in the 3-6 hr range, which would be sufficient to completely do/redo a whole task.

Can I request the model to rewrite the entire ref text in Rewrite Tasks?
If you request a re-write of the whole document there should be a constraint attached that limits length or asks the model to focus on just one part of the document since a lot of the time the model will not be able to generate such a long response. The recommendation is to focus on a specific section or part of the doc to avoid issues instead of the whole text, however using the whole text is possible like this.
Example:
I am writing a slide presentation on this 100000 word report, I need the content written to fit this presentation style. You should limit the slides to 10 and limit the content on each slide to 5 bullet points each. The tone of each bullet should be very casual. Please be sure to choose a title for each slide and provide it as bolded text prior to the bullet points.
Difference between the two:
Summary - A condensed version of the original text, focusing only on the main ideas and essential information while omitting details, examples, and elaborations.
Rewrite with Word Count/Length Limit - A rephrasing of the original text that conveys the same meaning or information in fewer words. This may still include all the original ideas, but in a more concise form. It isn't necessarily a summary unless it involves removing details or reducing the scope of information.
For example:
Original Text: "The cat, which was gray and small, leaped over the wooden fence with great agility and landed softly on the ground."
Concise Rewrite: "The small gray cat leaped over the fence with agility."
Summary: "The cat jumped over the fence."

Communication
Who do I communicate to? Who are my leaders?
You can post any question, concern, or issue you encounter in the Discourse channel Daily Thread, you just need to reply to our post.
If you're not in our channels, let us know through any syncs/workshops you receive an invite for in your Outlier Dashboard.
Your current Leaders (QMs) are Charmaine_N_QM, Nahomi_Garcia, Pablo_M_QM and Jack_J_QM in Discourse. Please don't send any DMs or Private Messages unless asked, just communicate through our Discourse channel.

