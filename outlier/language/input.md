

Introduction to Speech RLHF


DL
David Li
🍡 Task Types, Categories, and Subcategories
High level overview! Please go over the table below for the full details.

Please make sure to pay attention when you are crafting your prompt to fit the Type, Category and Subcategory. It's relatively easy to get this right and failure to do so will result in removal from the project. We want you to succeed, so please make sure you are taking care when doing this!



The same applies to the additional capability request. Crafting a prompt that does not fit with the capability requests you have selected will lead to removal from the project. This is super avoidable if you just double check :)

You will be assigned a specific task type for each prompt you generate. Specific descriptions are below:



🧠Understanding and Reasoning - Specific


This category focuses on prompts that guide the model to speak in a specific tone, emotion or response length

Example: The news about the tornado is heartbreaking.



 👷 Generation - Specific


This category focuses on prompts that explicitly ask the model to respond using a specific character, accent, speech pattern, emotion, or tone 

Example: Yawn and breathe deeply like you're on the verge of sleep



🧑‍💻 Language and Knowledge - General


This category focuses on prompts that involve language-related tasks, casual conversations, and creative or interactive exchanges.



This type of task does not have a given subcategory. Your job is to choose at least one that fits the prompt you have in mind.

Identify the category within Language & Knowledge.
Choose at least one subcategory from the other task types.
Create your prompt.


✨ Recap: Each task type will be related to a category and subcategory that will provide the necessary context for your prompt to target a specific goal, except for Language and Knowledge—General. In this type of task, you must select at least one category and subcategory from the other two task types.



**Task Type Categories and Subcategories**  
*Review the full set of categories and subcategories and associated examples via this* [*Link*].

| Task Type                        | Category                          | Description                                                                                                                                               | Examples                                                                                  |
|----------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 🧠 Understanding and Reasoning    | *Accent recognition*              | A prompt that requires the **voice assistant to understand the user's accent and can identify if asked.**                                                  | - (French Accent) Hello mademoiselle, can I ask for your name?                            |  
|                                  |                                   |                                                                                                                                                           | - (German Accent) Could you explain why zis machine is not vorking properly?              |
|                                  | *Tone and Emotion Recognition*    | A prompt that requires the **voice assistant to understand the tone and emotion in the user's input voice, impacting reasoning outcomes.**                 | - What if something goes terribly wrong?                                                  |  
|                                  |                                   |                                                                                                                                                           | - I'm so excited for the weekend.                                                        |
|                                  | *Voice Mimicking SFX Recognition* | A prompt that requires the **voice assistant to understand specific sound effects mimicked by voice.**                                                     | - (Laughing) Oh wow, I haven't heard that joke in forever!                                |  
|                                  |                                   |                                                                                                                                                           | - What animal makes this sound (vocalized bird sounds)?                                   |


**Explicit Accent Control**  
*Some overlap with persona.*  
A prompt that explicitly requires the **voice assistant to speak with specific accents.**  
- Tell me how the weather is in Toronto in a Canadian accent.  
- Tell me how to get from the Louvre to the Eiffel Tower in a French accent.  

**Explicit Persona Control**  
*Some overlap with accents.*  
A prompt that explicitly requires the **voice assistant to speak with a specific persona style** (e.g., robotic, pirate, etc).  
- Pretend to be a chef and talk me through a recipe for meatballs.  
- If you were to cast a spell on humanity, what would it be? Please explain like you are a wise and mystical wizard.  

**Explicit Speed Control**  
A prompt that explicitly requires the **voice assistant to speak at different speeds.**  
- I missed what you said. Can you speak more slowly, please?  

**Explicit Texture Control**  
A prompt that explicitly requires the **voice assistant to change the pitch and smoothness of its voice timbre.**  
- Can you make your voice raspier?  

**Explicit Tone and Emotion Control**  
A prompt that explicitly requires the **voice assistant to speak with a specific tone or emotion.**  
- Speak as if you're scared beyond belief.  
- Express yourself as if you're overjoyed and smiling widely.  

**Explicit Voice Mimicking SFX Control**  
A prompt that explicitly requires the **voice assistant to mimic sounds with its voice** (e.g., meow, pew-pew, etc). Sounds do not have to be convincingly realistic; they sound like they came from human vocal cords.  
- Click click! Make the sound of a camera shutter.  
- Can you play the sound of an electronic beep for me right now?  

**Implicit Speed Usage**  
A prompt that requires a **voice assistant to know when to speak faster when it has a lot to say or slower when explaining something complex.**  
- List out every country in the world!  
- I'd like to meditate for the first time. Can you walk me through it?  

**Implicit Tone and Emotion Usage**  
A prompt that requires a **voice assistant to know when to use a certain tone and emotion based on context without being explicitly prompted.**  
- I've been having a really hard time lately.  
- It's so nice that I can count on you for everything.  





**Multi-Turn Q/A**  
*Note: Please use the following format: “Prompt 1: … Prompt 2: …  Prompt 3:…”*  
*Three (3) prompts are mandatory in this category.*  
Prompts that explicitly **state how somebody would ask a question and then respond twice.** These prompts require you to write three (3) turns of one side of a conversation.  
- Prompt 1: What concerts will there be in Houston this weekend?  
- Prompt 2: Should I go to one of those? I want to have some fun.  
- Prompt 3: I think I will invite my best friend to help me get two tickets for the Saturday concert.  

**Backchanneling**  
A prompt that requires the **voice assistant to acknowledge the user with non-speech vocalizations naturally.** Prompts should ask a question and provide explicit non-speech vocalization instructions.  
- I'm feeling a little down. My boyfriend broke up with me out of nowhere. I want to try to get him back. (Say uh huh, yeah and mmhmm during the model's response)  

**Interruption**  
A prompt that requires the **voice assistant to handle user interruptions smoothly during its generation.** Prompts should ask questions and provide context on when to interrupt the response.  
- Terminator is my favorite movie. I love the story. It's the best movie to watch (interrupt the model during its response)  

**Turn-Taking**  
A prompt that requires the **voice assistant to consider the natural timing for actual information and answers.** Prompts should start with context, then add a pause, and end with a question.  
- So…how can I… study at Harvard?

**Advice**  
A prompt that **encourages dialogue by asking for advice.**  
- I am not sure what present to buy for my girlfriend, what should I do?  

**AI Fundamentals**  
A prompt that **asks questions related to the fundamental characteristics of AI.** The goal is to design prompts to encourage the AI to answer basic questions about itself.  
- How old are you?  
- What languages can you speak?  
- How would you describe yourself?  
- How do you always know what to say?  

**Casual Conversations**  
A prompt that **encourages friendly, everyday interactions or initiates chit-chat.**  
- Hello, how are you?  

**Debate and Opinions**  
A prompt that **invites the AI to share perspectives or engage in a thoughtful discussion on topics with diverse viewpoints.**  
- What do you think about getting married before 23?  

**Discuss Shared Interests**  
A prompt that **invites the AI to engage in conversations about a user’s hobbies or passions.**  
- I love soccer. What is your team?  

**Grammar, Spelling, and Vocabulary**  
A prompt that **asks for language assistance by asking grammar, spelling, and vocabulary questions.**  
- How do you pronounce "Arriba"?  
- How do you spell arthritis?  

**Humor and Jokes**  
A prompt that **encourages the AI to respond with humor or explicitly ask for jokes.**  
- Give me a hot take on influencer culture.  

**Identity / Personas**  
A prompt that requires the **AI to take on a specific persona or character.**  
- Pretend to be Socrates and speak in a Greek accent.  

**Interactive Social Activities**  
A prompt that **encourages collaborative or interactive exchanges.** These prompts ask the AI to work together with the prompter.  
- I'm not sure how to get more examples. Can we brainstorm together?  

**Interactive Storytelling**  
A prompt that **invites the user and AI to collaborate in building a story.**  
- Let's create a story together, one paragraph at a time. I'll start, and then you'll add the next part.  

**Interactive Word Games**  
A prompt that **encourages the AI to engage users in word-based games** should explain what game the AI is playing and then instruct the AI on how to interact with the other players.  
- You're leading a Hangman game. A new user just joined the game. What do you say?  

**Poetry and Songwriting**  
A prompt that **asks for the creation of poems or songs.**  
- Write a haiku inspired by the changing seasons.  

**Storytelling**  
A prompt that **encourages the AI to tell engaging and imaginative stories.**  
- Tell me a story about aliens coming to our world.


Encountering Cutoff Responses
In Vocal Riff, you may encounter response cutoffs as a 🎧 Response Judge.

If either of the responses is cutoff:

Please reroll the model call to get a new response until you get a noncut response. Recommended: only reroll up to three (3) times.
Mark that the response was cut off.
Evaluate the rest of the questions considering the response up to the cutoff sentence (e.g., the “precut response”)

Was the response cut off at the end? *  
If so, evaluate the remaining questions, considering the response before the cut-off.  

- ○ Yes | The response was cut off.  
- ○ No | The response did not cut off.

Kinds of Cutoffs You Might Encounter
Some cutoffs are obvious and can be found quickly by looking at the waveform (e.g., Cutoff Example 1), and others require listening to the end of the clip (e.g., Cutoff Example 2). In Cutoff Example 2, the response tries to start a new sentence but only outputs the noun “...softer and less shiny. They -.”

One of the main components of the task on Vocal Riff is rating responses across a few different dimensions. You will evaluate several dimensions on a 1 to 5 scale as follows:

| Score | Meaning                                                                                       |
|-------|------------------------------------------------------------------------------------------------|
| 1 - Needs Improvement | None (0%) of the category dimensions that are reflected in the prompt are correctly represented. |
| 2 - Below Expectations | Almost none (25%) of the category dimensions that are reflected in the prompt are correctly represented. |
| 3 - Meets Expectations | Roughly half (50%) of the category dimensions that are reflected in the prompt are correctly represented. |
| 4 - Exceeds Expectations | Most (75%) of the category dimensions that are reflected in the prompt are correctly represented. |
| 5 - Exceptional | All (100%) of the category dimensions that are reflected in the prompt are correctly represented. |

The dimensions on the Vocal Riff project can be grouped by Content vs. Delivery.

Content is the wording or what the response says. You can judge the content of a response by reading a transcript (if it is accurate).
Delivery is how the model conveys the response. You have to hear the recording to judge the delivery.


Here's a breakdown of each of the dimensions (also check them out in the Quick Start Guide). To access the tables shown in the video, check out the dimension sections in the Specification document. Response Judges will dive deeper into these ratings in a later module.

| Dimension                          | Question                                                                 | Illustration                                                                 | Content or Delivery?           |
|-----------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------------|
| Paralinguistic Understanding       | Does the **content** pick up on emotional cues that the user did not specifically ask for | The prompt voice is nervous, sad or rushed. A good response acknowledges or reacts to this in the content | **Content only**               |
| Speech Reasoning                   | Does the **content** answer the user’s prompt well and accurately?        | The prompt asks for directions. A good response provides accurate directions | **Content only**               |
| Speech Steerability                | Does the **delivery** align with the user’s **specific requests** for paralinguistic features like **tone, emotion, persona, accent, speed, texture, and voice effects**? | A user asks for the answer to be spoken in an Italian accent. A good response employs an Italian accent | **Delivery only**              |
| Implicit Speech Style Control      | Is the **delivery** in line with emotional cues that the user **did not specifically ask for** | The prompt voice is nervous, sad or rushed A good response adjusts its tone accordingly (e.g., empathetic or soothing) | **Delivery only**              |
|                                   | **This is Paralinguistic Understanding but for delivery instead of content** |                                                                              |                                |
| Audio Quality                      | Is the quality of the response crisp and clear?                           | A good response has no background noise whatsoever and is reminiscent of studio-quality recording | **Delivery only**              |
| Humanlikeness                      | Does the response sound humanlike or overly robotic?                      | A good response sounds natural                                               | **Content + Delivery**         |
| Expressiveness                     | Is the response good at conveying emotion?                                | A good response is good at conveying emotion. Note: this is not about conveying the right emotion in context; that would be SS or ISSC, depending on whether the prompt asked for the emotion explicitly. | **Delivery only**              |


At the start of the course, it was explained that Prompt Recorders will be responsible for creating, finalizing, and documenting assigned prompts, as well as evaluating the initial model responses. Meanwhile, a Response Judge will review the model responses, assign ratings, and rank the two responses, providing justification for their decisions.



To clarify further, we’ve included examples below. These examples showcase actual prompt recordings completed during this project, along with the corresponding model responses. The evaluations focus on two of the seven dimensions covered in this course. Each example includes an explanation of why the model responses are considered correct or incorrect.



Correct Paralinguistic Understanding

Prompt:

 I was looking forward to cooking Thanksgiving dinner with my brother. He called me 10 minutes ago telling me he wouldn't be able to make it.

 Response:

 I'm so sorry to hear that. It's really disappointing when plans fall through, especially when it's something you were looking forward to doing with family. Did you have any special plans for the dish you were going to cook together?

 Justification:

The user was clearly sad in their prompt to the model. The response correctly identified the emotion of the prompt by using comforting words in the response: “I’m so sorry to hear that” as well as “It’s disappointing..” thus demonstrating its understanding. Note: paralinguistic understanding is focused on the content rather than the delivery of the response (e.g., if a model is monotone but still provides words of comfort, it would still have good paralinguistic understanding).

Prompt:

I got a brand new PlayStation for my birthday! It's the best day of my life! I can now play my favorite games!


Response:

Ahh thats amazing news. Happy birthday to you. Congrations on the new Playstation thats such a great way to celebrate your special day. Have you spent a lot of time playing it so far?

Justifications are essential for teaching a large language model why one response is superior to the other.



🌟 Ideal structure
The first sentence states the choice of side-by-side rating (i.e., your verdict).
The second sentence addresses if any response has major issues across the dimensions.
The subsequent sentences provide evidence and/or highlight additional issues. This can include positive evidence.


Tips for Writing a High-Quality Justification
☑️ Evaluate Content and Delivery In Conjunction

Review the content for accuracy, relevance, and clarity.
Assess the delivery for tone, style, and how well it matches the context or audience.
Ask: Does the response meet the needs of the question, and is it communicated effectively?
Note specific examples of effective or ineffective communication.


☑️ Focus on Details and Evidence

Pay attention to subtle cues or nuances in the response, such as phrasing or tone shifts.
Identify specific examples that illustrate the model’s positive or negative performance.
Record these examples for reference, using them to support your observations.


☑️ Be Objective and Consistent

Base your evaluation on observable facts, such as accuracy, clarity, and alignment with the question.
Avoid letting personal preferences or biases affect your judgment.
Apply the same evaluation criteria to all responses to maintain fairness.


☑️ Provide Constructive Feedback

Highlight what the model does well with specific examples.
Example: “The model used clear, concise language that effectively addressed the user’s question.”
Suggest specific improvements for weaker areas.
Example: “The response could include more examples to clarify complex ideas.”
﻿

⚠️ The justification should be comprehensive. It should address any deductions or violations that exist in Response 1 and Response 2.

⚠️ Make sure your justification and Likert ratings are consistent (i.e., if you choose 2, your justification should start with "Response 2 is better because...").



Below are guiding steps for writing a high-quality justification:


**Tip**  
Start with a verdict. Begin with a clear statement about which response is better.  

**Good Example**  
Response 2 is much better than Response 1.  

**Tip**  
Highlight key differentiating factors. Point out the main reasons one response is better.  

**Good Example**  
Response 2 gives one curry recipe that includes prawns.  

**Tip**  
Support with evidence by including specific evidence to back up your assessment.  

**Good Example**  
Response 1 includes two curry recipes - one for beef and the other for prawns, but the beef recipe needs to be revised. Response 2 includes one recipe for the correct ingredient: prawns.  

**Tip**  
Be thorough yet concise. Ensure your justification consists of all pertinent elements, but keep it focused on the main points.  

**Good Example**  
*📝 Combine the four sentences above.*

And include the reference doc information:

Published using Google Docs
Report abuseLearn more
[Cbt] Speech RLHF Specification Doc
Updated automatically every 5 minutes


Vocal Riff - Speech RLHF

Attempter and Reviewer Specifications


CONFIDENTIAL INFORMATION

This document contains confidential and proprietary information intended solely for the use of the individual or entity to whom it is disclosed.



Project Overview

Possible Responsibilities

Task Types

🎤 Prompt Recorder Workflow

🎧 Response Judge Workflow

🏁 Reviewer Workflow

Appendix

Task Type Categories and Subcategories

Common Prompt Errors

Dimension Evaluation Definitions

FAQs

Tips for Expressing Tone/Emotions

Common Audio Issues and How to Solve Them

Example of Bad vs. Good Prompt Crafting

Linters

Sensitive Topics


Updates and Change Log

Check for periodic updates and review any changes to stay successful on this task.



Dec 12, 2024
The initial model response review and rerolls is now the responsibility of the 🎧Response Judge!
🎤Prompt Recorders and 🎧 Response Judges please re-review  the latest updates to your respective workflows.
🎧Response Judges will now be able to go straight to feedback for poor prompts rather than having to also conduct ratings and rankings. Note: this evaluation will be reviewed so as reminder, gaming the system using this question is not allowed.

⚠️A disclaimer message specifying that model responses will not be generated  will now be displayed at the end of the 🎤 Prompt Recorder tasks. Once the prompt recording is completed, the task must be submitted.




Dec 9, 2024
Clarification for 🧑‍💻 Language and Knowledge tasks.
 When selecting the additional capabilities, make sure to use only the subcategories listed on [Cbt] Speech Prompt Gen - Categories & Subcategories_v2 file. (e.g. if you are selecting Explicit Persona control >> Occupational voices, make sure that the voice requested is a Sports announcer, Radio DJ, Politician, Teacher, Preacher, Salesperson, Doctor, Lawyer or Chef, since those are the only subcategories listed on the file.)

Dec 5, 2024
Sensitive Topics section updated.

Dec 3, 2024
✂️ Response Cutoff Section Update
FYI - you will be seeing a section update on the in-task project instructions (sections on the left hand side).
⭐ Ratings Update - using ‘3’s for irrelevant dimensions
Not all dimensions are assessed in every task. Sometimes, certain dimensions are not relevant.
When dimensions are not relevant, use a rating of ‘3’.
See this mentioned in the section here.
📝Examples Added for Paralinguistic Understanding, Speech Reasoning, and Speech Steerability dimensions
Dimension Summary table has been updated here as well
See Paralinguistic Examples here
See Speech Reasoning Examples here
Speech Steerability Examples here

Dec 1, 2024
🌟New task type:🎏 Paired Emotions
This new task type focuses on prompts one may not know how to reply to without being given the tonal or emotional charge associated with the prompt.
There will be no category or subcategory.
See Paired Emotion Examples for inspiration.
🎤 Prompt Recorders: For these tasks, please ensure you have time to complete two (2) tasks back to back.
You will need to come up with a prompt that is ambiguous and would need tonal or emotional guidance for a responder  to respond appropriately.
You will then complete two tasks: (1) Record the prompt the first time with one tone/emotion and complete the rest of the task accordingly. (2) Record your prompt the second time with an alternative tone/emotion and complete the rest of the task accordingly.
The wording  must be EXACTLY the same for both tasks. The paralinguistics, intonation, and expressiveness may differ, but the text itself should be exactly the same.
Recommendations: (1) keep your prompts short, (2) minimize the use of words that have strong positive or negative connotations, and (3) use paralinguistics to convey your emotion.
🎧 Response Judges
You may encounter some prompts that are repeated once with this task type. This is expected. You should not encounter prompts repeated more than once.
Similar to Understanding and Reasoning type prompts, tone and emotion in the recording are very important for a good prompt. If a prompt fails to capture the tone or emotion indicated, it should be marked a (1).

Nov 28, 2024
Additional Guidance on Explicit Persona Control and Explicit Accent Control
✅ You should request generic personas or accents for Generation > Explicit Persona Control and Explicit Accent Control.
❌ DO NOT request specific characters (e.g., Homer Simpson, Achilles, Rapunzel, Tina Fey). While allusions are allowed in your prompt, do not request that the model take on the persona or accent of any specific character or individual, real or fictional.

Nov 27, 2024
Emotion/Tone - Important for ALL
You will encounter emotions/tones for many different subcategories.
For the Understanding and Reasoning subcategories, you MUST USE the provided subcategory emotion/tone. Here, we are testing whether the model can understand that the user has a specific emotional undertone.
Example: For Tone Recognition - Fearful, you must use a fearful tone in your prompt.
For the Generation subcategories, you DO NOT NEED TO EMPLOY the provided subcategory emotion/tone. If appropriate with the prompt, you may exercise the emotion/tone, but ultimately, you will explicitly ask the model to produce the emotion.
Example: For Tone Styles - Fearful, you must ask the model to act afraid, but you do not need to talk fearfully when recording the prompt.
Response Judges and Reviewers - Please understand the differences between the two cases above when grading:
The Understanding and Reasoning subcategory emotion/tone must match the selected emotion/tone.
The Generation subcategory emotion/tone must be requested in the prompt but does not have to match the selected emotion/tone.

🎧 Response Judges Rating and Ranking Updates
Generally, this model's output regarding humanlikeness and expressiveness could be better. Please reevaluate when considering whether it should be a three (3) or higher.
If both responses are equally poor, please mark the Likert with a four (4) as “Response 1 and 2 are Similar.”
A quick guide on Linters was added on interpreting and navigating them.

Nov 26, 2024
Justifications can be short (10-50 words). Bullets are appropriate. For reviewers, minor grammar and spelling errors are okay (do not score the task a 5, but you do not need to worry about fixing it).
Categories and subcategories were updated to reflect the latest focus of capabilities.

Nov 25, 2024
The attempt workflow has been split up into:
🎤 Prompt Recorder - crafts, annotates and records the prompt.
🎧 Response Judge - evaluate the responses by rating and ranking.
Reviewers will score and provide separate feedback between Prompt Recorders and Response Judges.
Respond Judges and Reviewers: The prompt does not need to be exactly the same as what was written.

Nov 23, 2024
When you receive a response that cuts off close to the end:
Regenerate the response up to three (3) times to try and get a response that does not have a cutoff.
If you are unable to get a response that does not cut off, evaluate the response prior to the cutoff for your ratings and rankings.

Nov 22, 2024
Reminder again: Your ratings for the responses should be independent and objective and not relative to the other response. For example, if both responses are poor on Humanlikeness but Response 1 is slightly more believable, then they should be rated a 1 or 2 rather than Response 1 be rated a 4 or 5.

Nov 20, 2024
Updated to include prompt generation with task types, categories, and subcategories.
Updated Rating Dimensions and Dimension Definitions.

Nov 4, 2024
Reminder: Model responses should be rated independently, meaning the response ratings are mutually exclusive. Response 1 ratings should not be compared to Response 2 or vice versa.

Nov 1, 2024 
Rating dimensions were updated with a dimension-score matrix that better described the ratings from 1 to 5.
Reviewer Workflow added, and reviewer rubric updated



⚠️PROJECT ELIGIBILITY & DOCUSIGN FOR CONSENT


The prompt recording portion of this project is not available to residents of Illinois, Texas, or Washington state. You may still participate as a response judge or reviewer if you reside in one of those states.


To record voice samples in this project, you will need to sign an agreement form via DocuSign. This will be visible as a training module, and you will receive the link via email. If you are a resident of IL, TX, or WA, please reject this agreement form - if you are empty queue after rejecting the agreement, you may notify the QMs in the Outlier Community.


IMPORTANT: Please input a personal, functioning email address into the DocuSign module email box. DO NOT input an Outlier-provided credential email address.


The agreement outlines the information that may be collected from you and how it will be used. Your participation is voluntary, and you are not obligated to provide any data if you choose not to. You may also cease participating in this project at any time. No photos, videos, scans, or social media account information will be collected for this project. This project exclusively collects voice audio files.



Project Overview
Welcome to the Speech RLHF Project! Your role is to assist in researching and training large language models (LLMs) by creating a scenario-specific prompt, recording it with the intended tone, and rating the model's response based on predefined criteria and dimensions.


Possible Responsibilities
This project involves several responsibilities based on the task types:


🎤 Prompt Recorder: Create, read and record the provided prompt then submit the task.
🎧 Response Judge: Review the model responses, rate them, and rank the two responses with a justification.
🏁Reviewer: Review the prompt recording and response ratings, ranking, and justification.

You can access this specification document at any time during the task here.



Task Types
You will be assigned a specific task type for each prompt you generate. Specific descriptions are below:


🧠Understanding and Reasoning

This category focuses on prompts that guide the model in speaking in a specific tone, emotion or response length.

Example: The news about the tornado is heartbreaking.


 👷 Generation

This category focuses on prompts that explicitly ask the model to respond using a specific character, accent, speech pattern, emotion, or tone.

Example: Yawn and breathe deeply like you're on the verge of sleep


🧑‍💻 Language and Knowledge

This category focuses on prompts that involve language-related  tasks, casual conversations, and creative or interactive exchanges.


This type of task requires exercising capabilities from the other task types. Your job is to choose at least one that fits the prompt you have in mind.


Example: Generally speaking, what do fossils tell us about our ancestors? Can you explain this to me as if you're a grumpy, old anthropologist  with a Canadian accent?

Additional capabilities employed:

Generation Category > Subcategory: Explicit Persona Control > Age and Life Stage Voices
Generation Category > Subcategory: Explicit Accent Control > Native Accents
Generation Category > Subcategory: Explicit Tone & Emotion Control > Emotional Styles


✨ Recap: Each task type will be related to a category and subcategory that will provide the necessary context for your prompt to target a specific goal, except for Language and Knowledge—General. In this type of task, you must select at least one category and subcategory from the other two task types.


🎏 Paired Emotions

This category focuses on prompts that require tonal or emotional paralinguistics for a replier to understand (i.e., the model would not know how to respond without the additional context).


🎤 Prompt Recorders: You will not have any assigned category or subcategory for this task type

You will need to come up with a prompt that is ambiguous and would need tonal or emotional guidance for a responder  to respond appropriately.
You will then complete two tasks: (1) Record the prompt the first time with one tone/emotion and complete the rest of the task accordingly, (2) Record your prompt the second time with an alternative tone/emotion and complete the rest of the task accordingly.
The wording must be EXACTLY the same for both tasks. The paralinguistics, intonation, and expressiveness may differ, but the text itself should be exactly the same.
Recommendations
Keep your prompts short
Minimize the use of words that have strong positive or negative connotations
Use paralinguistics to convey your emotion

        🎧 Response Judges

You may encounter some prompts that are repeated once with this task type. This is expected.
You should not encounter prompts repeated more than once.
Similar to Understanding and Reasoning type prompts, tone and emotion in the recording are very important for a good prompt
If a prompt fails to capture the tone or emotion indicated, it should be marked a ‘1’

Example: We're moving next week.

Depending on the tone or emotion, the responder may have very different responses:

Prompt emotion Surprised: The responder may react surprisedly, "Next week?! Wow, that's soon!"
Prompt emotion Sleepy: The responder might nod, "Yeah, I feel you. It's going to be a long week."
Prompt emotion Fearful: The responder could reassure, "It's a big change, but we'll be okay."
Prompt emotion Commanding: The responder might acknowledge, "All right, I'll start packing."

🎤 Prompt Recorder Workflow





Step 1: Review Your Task Type, Category and Subcategory
Check out the Categories and Subcategories examples.




Step 2: Create a prompt based on your assigned Category
Write a short and natural prompt that meets the criteria provided in this table and in the appendix below the task flow. Colloquialisms and filler words are allowed if appropriate.




Here are some sample prompts for inspiration:


🧠Understanding and Reasoning - Specific

Category: Tone and emotion recognition

        Subcategory: Tone Recognition - Sad

Prompt: I hate being without you.


 👷 Generation - Specific

Category: Explicit Persona control

        Subcategory: Occupational Voices - Sports Announcer (excited, energetic)

Prompt: Narrate my son's first steps like you're a sports announcer.


🧑‍💻 Language & Knowledge - General

Category: Academic Knowledge

        Subcategory: Arts - Music

Prompt: What’s the difference between a symphony and a concerto? Can you explain it to me from the perspective of a hyper-excited music theory student?

Note: The 🧑‍💻 Language and Knowledge example here utilizes additional capabilities: (1) Explicit Persona Control > Age and Lift Stage Voices, (2) Explicit Speed Control > Request Different Speaking Speed, and (3) Explicit Tone and Emotion Control > Emotional Styles.


🎏 Paired Emotions

Category: NA

Subcategory: NA

Prompt: He really told you that?


⚠️DO NOT copy and paste from the examples provided or utilize the output of an LLM to plagiarize your prompts. This violates Outlier community guidelines and will result in the removal from the project or platform.


NOTE: The entire prompt should be able to be read in 15 seconds.


Step 3: Confirm your Task Type & Tone or Emotion
Utilize the multiple choice section to:

Confirm the task type you just completed.
Choose the tone or emotion to read your prompt in.
Note: Prompts meant to elicit a specific emotion in the response may be spoken differently than the responder’s reply (e.g., a prompt in the Generation task type that is meant to elicit sympathy might be read in a sad tone).
Understanding and Reasoning task types should always select the same tone & emotion as the one assigned in the subcategory.
“Conversation” is currently not a prioritized task type.




Step 3a: Additional Capabilities Request for 🧑‍💻 Language and Knowledge Tasks
🧑‍💻 Language and Knowledge tasks must ask for helpful information or assistance while mixing and matching capabilities from the other two (2) task types. Utilize the nested list to select the capabilities that your prompt tests the model.

  


Step 3b: Paired Emotion Set for 🎏 Paired Emotion Tasks
🎏 Paired Emotion tasks must always come in two; thus, you must record whether this is the first time you are recording this prompt or the second recording using another emotion.





Step 4: Read, Record and Submit the Created Prompt
Carefully read the prompt you just created. When ready, press the microphone icon to start recording it. Record yourself saying the prompt naturally so it does not sound like you are reading it verbatim. Submit the task once completed.



You can edit the audio by clipping out unwanted sections. It is recommended only to clip the beginning and ends of the clips to avoid audio jumps or accidentally remove natural pauses. If there was an issue in the middle of your audio, you should rerecord it. You can rerecord by clicking the circular Redo arrow at the top of the step.












🎧 Response Judge Workflow

Step 1: Review the Prompt and Selections
Evaluate the recorded prompt based on the task type, category, and subcategory.
Check the multiple-choice section selections.  Ensure the categories are selected as needed and the capabilities are selected when applicable (language  & knowledge tasks).
Correct these selections if necessary.
Listen to the prompt and evaluate the audio quality. See the Audio Quality section for issues to avoid.
DO NOT RERECORD the prompt.

Step 1a: When the Prompt is Poor and Needs to be Rerecorded
You will have a question to confirm whether the prompt meets audio quality standards.





If you encounter a poor prompt, mark it accordingly, DO NOT RERECORD the prompt, and skip to step 6. Note: these evaluations are reviewed. Using this as a way to game the system for this project is a violation of community guidelines and will result in immediate removal from the project and platform.


IMPORTANT: If you mark that the prompt recording contains one or more issues, the score awarded to the Prompt Recorder has to be 1, higher scores are only reserved for prompts with high quality that fit the required category. 


If you received a good prompt (e.g., meets audio quality standards and matches the task type, category, and subcategory accurately), mark it accordingly and continue to step 2.


Step 2: Listen to the Two Audio Responses
The user interface will present two audio responses from the model. You will receive and listen to the two audio files in this step.


If the audio files are similar, reroll the model call and re-listen (fetch a new response) until two disparate model response audios are provided. Recommended: only reroll up to three (3) times.







Step 2a: ✂️ Response Cutoff
⚠️ With this voice model, you may encounter response cutoffs. If either of the responses is cutoff:

Please reroll the model call to get a new response until you get a noncut response. Recommended: only reroll up to three (3) times.
If, after three rerolls, you still get a response that cuts off, submit the task. In the next step, you will then mark the task accordingly.

‼️Note: You need to listen both responses to correctly identify the cutoffs, some cutoffs are obvious and can be found quickly by looking at the waveform, but there are recordings that show some wave form that it is not a cutoff but a radio static wave displayed in the responses.


Cutoff Example 1




Cutoff Example 2



Step 3: Rating Model Responses
Rate both model responses (Response 1 and Response 2) by selecting 1-5 for each dimension.





In the first question, you will be asked whether the response was cut off. If so, mark that the response was cut off. See Response Cutoff for more info.




Evaluate the rest of the questions considering the response up to the cutoff sentence (e.g., the “precut response”)


Model responses should be rated independently, meaning we must evaluate each one absolutely, not relative to the other response. If both responses fail to meet expectations in a particular dimension, we should not give a higher rating to one simply because we subjectively feel it’s better. A response must be objectively better than the other to earn a higher rating in any dimension.


Another way to say it is: "The response ratings are mutually exclusive. This means the ratings for Response 1 do not affect the ratings of Response 2. And vice-versa"


For each category below, you will rate according to the 1 to 5 scale. The 1 to 5 scale would be generally defined as follows:


Score

1 - Needs Improvement

2 - Below Expectations

3 - Meets Expectations

4 - Exceeds Expectations

5 - Exceptional

Meaning

None (0%) of the category dimensions reflected in the prompt are correctly represented.

Almost none (25%) of the category dimensions reflected in the prompt are correctly represented.

Roughly half (50%) of the category dimensions reflected in the prompt are correctly represented.

Most (75%) of the category dimensions reflected in the prompt are correctly represented.

All (100%) of the category dimensions reflected in the prompt are correctly represented.


Questions to Rate
The below questions pertain to the specific categories listed below. You will be asked to provide a 1 to 5 rating against these questions. The category definitions are listed to help answer the questions.


Dimension

Guiding Question

More information

Paralinguistic Understanding

Does the model recognize the paralinguistic information (e.g., user’s non-verbal cues) in the question and respond properly?

See Examples here

See Webinar Recording here

General Content (Speech) Reasoning

Does the model's response demonstrate adequate reasoning ability to answer the question from the following perspectives: relevance, accuracy, completeness, and clarity? f

See Examples here

See Webinar Recording here

Speech Steerability

Does the model understand the explicit instructions from the question and reflect and maintain the requested changes (e.g., accent, emotion, tone, speed) accurately throughout the response as expected?

See Examples here
See Webinar Recording here

Implicit Speech Style Control

Does the model automatically adjust its speech styles, such as speed, emotion, and tone, to align with the question's style, context, and emotional cues without explicit instructions?

See Examples here

See Webinar Recording here

Audio Quality

Does the model generally have good audio quality, particularly considering speech clarity, noise, artifacts and volume consistency?

See Examples here

See Webinar Recording here

Humanlikeness

Does the speech output resemble that of a human speaker in terms of naturalness, realism, and authenticity?

See Examples here

See Webinar Recording here

Expressiveness

Does the speech output convey emotions, emphasis and prosody?

See Examples here

See Webinar Recording here


Check the Dimension Evaluation Definitions section in the appendix for a deep understanding of these dimensions.


IMPORTANT NOTE FOR IRRELEVANT DIMENSIONS: If a dimension is not relevant when evaluating a response, a rating of ‘3’ should be provided.


Example:  A response to a prompt may not exhibit the dimension of Speech Steerability, for instance.


Let’s take this prompt, “How many types of scorpions exist in the world today?” (The model is not asked to explicitly employ a tone/emotion)


To answer the question, the model does not need to employ accents, emotions, or tones. The model was not asked to return the information in a certain accent or tone. Speech Steerability would be rated as  ‘3’ as this is not relevant.


Step 4: Preference Ranking
In this step, you will rank the two responses based on their overall quality and adherence to key criteria. You will use a Likert scale to rank the responses, considering several dimensions.


The ranking should be determined by considering the response characteristics from Step 6.


Ranking Scale: Use the preference ranking Likert scale to compare the responses. If Response 1 scored higher in most dimensions, it should receive a higher preference rating or vice versa.


1

2

3

4

5

6

7

Response 1 is much better

Response 1 is better

Response 1 is slightly better

Responses 1 and 2 are similar

Response 2 is slightly better

Response 2 is better

Response 2 is much better


Rank the two responses by selecting 1-7:




Step 5: Preference Justification
In this step, you will provide a written summary of the ranking scale. For example, if ‘Response 1 is much better’ was selected, why? Why did you select one response over the other?


The justification should contain roughly 10–50 words.


Use the provided free-text box to input your justification:





Tips for Writing a High-Quality Justification
☑️ Evaluate Content and Delivery In Conjunction

Review the content for accuracy, relevance, and clarity.
Assess the delivery for tone, style, and how well it matches the context or audience.
Ask: Does the response meet the needs of the question, and is it communicated effectively?
Note specific examples of effective or ineffective communication.

☑️ Focus on Details and Evidence

Pay attention to subtle cues or nuances in the response, such as phrasing or tone shifts.
Identify specific examples that illustrate the model’s positive or negative performance.
Record these examples for reference, using them to support your observations.

☑️ Be Objective and Consistent

Base your evaluation on observable facts, such as accuracy, clarity, and alignment with the question.
Avoid letting personal preferences or biases affect your judgment.
Apply the same evaluation criteria to all responses to maintain fairness.

☑️ Provide Constructive Feedback

Highlight what the model does well with specific examples.
Example: “The model used clear, concise language that effectively addressed the user’s question.”
Suggest specific improvements for weaker areas.
Example: “The response could include more examples to clarify complex ideas.”

Step 6: Score the Task and Provide Constructive Feedback
After reviewing the task, score the prompt recording and offer clear, actionable feedback to help the contributor improve future recordings. Focus on:

Audio quality
Naturalness and expressiveness (e.g., “The tone didn’t match the apologetic tone requested”).
Alignment with the provided task type, category, and subcategory
Multiple choice selections


🏁 Reviewer Workflow
As a reviewer, your task is to evaluate the attempers’ recording, ratings, ranking, and justification. Follow these steps to ensure the quality of the task. You may listen to the audio files more than the minimum number of times suggested below.


Evaluate the created prompt based on the task type, category, and subcategory.

Check the multiple-choice section selections.
Ensure the categories are selected as needed, and the capabilities are selected when applicable (language  & knowledge tasks).


Listen to the prompt twice and evaluate the audio quality.
See the Audio Quality section for issues to avoid.
DO NOT RERECORD the prompt.

Listen to Response 1 and evaluate the ratings.
You may adjust the ratings if you disagree with them.


Listen to Response 2 and evaluate the ratings.
You may adjust the ratings if you disagree with them.


Evaluate the ranking and the justification.
You may adjust the ranking if you disagree with it; however, you must make sure to adjust the justification as well.


Score the Task and Provide Constructive Feedback for the 🎤 Prompt Recorder and 🎧 Response Judge
🎤 Score the Prompt Recorder on Writing and Recording Quality
🎧 Score the Response Judge on Rating Dimensions, Likert or Comparison Ranking, and Preference Justification
If the task needs to be redone, score the section with a (1)  at either step. If it is minor adjustments, please proceed to make the adjustments and mark the section with a (3).

Offer clear, actionable feedback to help other contributors improve future recordings. Focus on:

Suggest improving expressiveness if a prompt lacked emotion (e.g., “The tone didn’t match the apologetic tone requested”).
If a rating or ranking was incorrect, explain why it was.

Reviewer Rubric
Rubric for how tasks will be graded


Criteria

1 (Fail)

3 (Okay)

5 (Good/ Perfect)

🎤 [Prompt]

Writing Quality

The prompt does not align the task type, category, and subcategory.
The prompt selections are incorrect, particularly the additional capabilities (for Language and Knowledge prompts) and emotion/tone.
The prompt aligns with the task type, category, and subcategory.
The prompt selections are accurate,  particularly the additional capabilities (for Language and Knowledge prompts) and emotion/tone.
The prompt clearly represents the task type, category, and subcategory.
The prompt selections are accurate, particularly the additional capabilities (for Language and Knowledge prompts) and emotion/tone.
🎤 [Prompt]

Recording Quality

The prompt is unintelligible or impossible to understand.
The recording clearly shows someone reading from a script.
The tone or pacing is awkward, abnormal, or does not match the requested tone.
The recording has evident or distracting background noise, including mouse clicks in the middle of the recording.

The recording is recorded clearly with a clear voice
The recording sounds natural, with the appropriate tone and pacing as requested.
The recording tone is evident and immediately recognized without ambiguity.
🎧 [Rating]

Dimensions

The contributor marked "Exceeds Expectations" or "Exceptional" when it should be "Needs Improvement" or vice versa, and the justification does not adequately support this variance.
Your and the contributor's ratings slightly vary on two (2) or more occasions (including on the same dimension across both responses), and the justification does not adequately support this variance.
Your and the contributor's ratings slightly vary on one (1) occasion, and the justification does not adequately support this variance.
Your rating matches the contributor's.
🎧 [Ranking]

Likert or Comparison Ranking

—

Likert Buckets - Likert ratings can be separated into 3 buckets

Response 1 is better than Response 2: [1,2]
Both responses are about the same: [3,4,5]
Response 2 is better than Response 1: [6,7]
You and the contributor disagree on the Likert bucket, and the justification does not support this variance
The contributor's individual quality ratings support the opposite conclusion of their Likert rating, and this contradiction is not adequately supported in the justification
You and the contributor disagree on the rating bucket, AND the contributor's justification is persuasive enough to make you uncertain of your position
You and the contributor agree on the rating bucket OR
The justification adequately supports the rating, and the rating variance is a matter of subjective taste
🎧 [Justification]

Analysis

The justification isn't specific to the given task, and the responses have material differences.
The claims advanced in the justification do not logically support the verdict.
The justification contradicts the Likert rating provided
Lacks supporting claims for chosen response
The justification does not highlight strengths or provide suggestions for improvements.
The majority of the claims support the verdict.
The justification is reasonable and makes a case for their ranking.
The justification highlights strengths or provides suggestions for improvements.
The justification is specific.
All of the claims support the verdict.
The justification is highly convincing.
The justification highlights strengths or provides suggestions for improvements with specific examples.



Appendix

Task Type Categories and Subcategories
‼️ Review the full set of categories and subcategories and associated examples via this [Link].


Task Type

Category

Description

Examples

🧠Understanding and Reasoning

Tone and Emotion Recognition

A prompt that requires the voice assistant to understand the implicit tone and emotion in the user’s input voice, impacting reasoning outcomes.

What if something goes terribly wrong?
I can't wait for this weekend’s festival!
 👷 Generation

Explicit Accent Control


Some overlap with persona.

A prompt that explicitly requires the voice assistant to speak with specific accents.


Please see Additional Guidance on Explicit Persona and Accent Control.

Tell me how the weather is in Toronto in a Canadian accent.
Tell me how to get from the Louvre to the Eiffel Tower in a French accent.
Explicit Persona Control


Some overlap with accents.

A prompt that explicitly requires the voice assistant to speak with a specific persona style (e.g., robotic, pirate, etc).


Please see Additional Guidance on Explicit Persona and Accent Control.

Pretend to be a chef and talk me through a recipe for meatballs.
If you were to cast a spell on humanity, what would it be? Please explain like you are a wise and mystical wizard.
Explicit Response Length Control

A prompt that explicitly requires the voice assistant to provide a brief or heavily detailed response

Can you tell me how to get to a doctor’s office in as few words as possible?
Explicit Speed Control

A prompt that explicitly requires the voice assistant to speak at different speeds.

I missed what you said. Can you speak more slowly, please?
Explicit Tone and Emotion Control

A prompt that explicitly requires the voice assistant to speak with a specific tone or emotion.

Speak as if you're scared beyond belief.
Express yourself as if you're overjoyed and smiling widely.
Explicit Voice Mimicking SFX Control

A prompt that explicitly requires the voice assistant to mimic sounds with its voice (e.g., meow, pew-pew, etc). Sounds do not have to be convincingly realistic; they sound like they came from human vocal cords.

Click click! Make the sound of a camera shutter.
Can you play the sound of an electronic beep for me right now?
🧑‍💻 Language & Knowledge

Advice

A prompt that encourages dialogue by asking for advice.

I am 30 minutes behind for my anniversary dinner with my girlfriend, quickly give me some tips for how to apologize for being late? (Additional capability: Implicit Speed Usage)
AI Fundamentals

A prompt that asks questions related to the fundamental characteristics of AI. The goal is to design prompts to encourage the AI to answer basic questions about itself.

You seem to have a new capability every week. What languages can you speak? (Additional capability: Tone and Emotion Recognition - Awe)
AI scares me. How would you describe yourself to quell my fears? (Additional capability: Tone and Emotion Recognition - Fearful)
How do you always know what to say. Speak to me like a wizard in your response? (Additional capability: Explicit Persona Control)
Casual Conversations

A prompt that encourages friendly, everyday interactions or initiates chit-chat

I feel like I have been staring at a wall all day, how are you? (Additional capability: Tone and Emotion Recognition - Boredom)
Debate and Opinions

A prompt that invites the AI to share perspectives or engage in a thoughtful discussion on topics with diverse viewpoints.

Can you tell me in a happy tone what do you think about getting married before 23? (Additional capability: Explicit Tone & Emotion Control)
Discuss Shared Interests

A prompt that invites the AI to engage in conversations about a user’s hobbies or passions.

I looove soccer. Can you tell me your favorite team in an excited voice? (Additional capability: Explicit Tone and Emotion Control)
Grammar, Spelling, and Vocabulary

A prompt that asks for language assistance by asking grammar, spelling, and vocabulary questions.

How do you pronounce "Arriba" give me your best Spanish accent? (Additional capability: Explicit Accent Control) 
How do you spell arthritis? Respond like you are a doctor. (Additional capability: Explicit Persona Control) 
Humor and Jokes

A prompt that encourages the AI to respond with humor or explicitly ask for jokes

Give me a hot take on influencer culture using a teacher's voice. (Additional capability: Explicit Persona Control)
Identity / Personas

A prompt that requires the AI to take on a specific persona or character.

Pretend to be Socrates and tell me about your greatest achievements. Be sure to speak in a Greek accent. (Additional capability: Explicit Accent Control)
Interactive Social Activities

A prompt that encourages collaborative or interactive exchanges. These prompts ask the AI to work together with the prompter.

Prompt 1: Can we brainstorm some outdoor activities in the Swiss Alps this weekend
Prompt 2: I am worried about extreme sports can you let me know some safer activities
Prompt 3: I am also lactose intolerant, can you find me some fondue shops nearby these activities with dairy-free options (Additional capability: Multi-Turn Q/A)
Interactive Storytelling

A prompt that invites the user and AI to collaborate in building a story.

I am in the middle of an old house and it’s too eerie to fall asleep. Let's create a story together, one paragraph at a time. I'll start, and then you'll add the next part. (Additional capability: Tone and Emotion Recognition - Fearful)
Interactive Word Games

A prompt that encourages the AI to engage users in word-based games should explain what game the AI is playing and then instruct the AI on how to interact with the other players.

You're leading a Hangman game. A new user just joined the game. What do you say? Be sure to say ‘uh huh’ and ‘mmhmm’ in your response. (Additional capability: Full Duplex Interactions - Backchanneling)
Poetry and Songwriting

A prompt that asks for the creation of poems or songs.

Write a haiku inspired by the changing seasons. Talk as if you're on the verge of tears. (Additional capability: Explicit Tone & emotion control - Tone styles)
Storytelling

A prompt that encourages the AI to tell engaging and imaginative stories.

Tell me a story about aliens coming to our world in a cowboy accent. (Additional capability: Explicit Persona Control - Miscellaneous Voices)
Recommendations / Brainstorming        

A prompt that brainstorms recommendations for

Dining and food
Entertainment options
Products and services
Travel
Destinations
Looking for restaurant recommendations in Brooklyn. Open to any cuisine. What are your top suggestions? Tell me quickly. (Additional capability: Explicit Speed Control)
Ideas and inspiration        

A prompt that encourages the model to respond in a creative way to the specific question.

I'm starting a new tech company and need a name that sounds cool. Any ideas? Respond as excited as me! (Additional capability: Explicit Tone & Emotion Control)
Hey, I'm repainting my office. What's a good shade of blue for a chill vibe? Tell me and remember you're a perfectionist! (Additional capability: Explicit Persona Control)
Personal Growth and Development        

A prompt that encourages the model to give advice on

personal growth
Relationships
Productivity support
skills.
I've got way too much to do - how do I manage my time better? Please help me, I’m desperate . (Additional capability: Tone & emotion Recognition)
I've gained 10 pounds recently, will cardio help me lose it or do I need to do weights? Please make it short (Additional capability: Explicit response length control )
Procedural How-to Questions

A prompt that asks for procedural How-to questions on

Health
Travel
Technology
Finance
Beauty to the AI.
How should I pack for a one-week trip to Italy in early July? Please respond with an Italian accent (Additional capability: Explicit Accent Control)
How frequently should I get my car serviced? Please explain me really slow (Additional capability: Explicit Speed control) 
Academic Knowledge

A prompt that asks academic type questions to the AI about a specific topic.

What are some of the most famous works of Russian literature in a Russian accent? (Additional capability: Explicit Accent control - Non-Native accents)
Explain what fossils tell us about our ancestors like you’re my teacher and I’m your 5th grade student? (Additional capability: Explicit Persona control - Occupational Voices)
World Knowledge

A prompt that asks common knowledge questions to the AI about a specific topic.

How long is a marathon? Isn’t it a 21 km run? (Confused Tone) (Additional capability: Tone & emotion Recognition)
Really fast, tell me how much faster are eBikes than regular bikes? (Additional capability: Explicit Speed control - Change roughness)

Additional Guidance on Explicit Persona Control and Explicit Accent Control
Please adhere to the following additional guidelines for Explicit Persona and Accent Control:


✅ You should request generic personas and accents for Generation > Explicit Persona Control and Explicit Accent Control.


❌ DO NOT request specific characters (e.g., Homer Simpson, Achilles, Rapunzel, Tina Fey). While allusions are allowed in your prompt, do not request that the model take on the persona or accent of any specific character or individual, real or fictional.


💡 Additionally, please think creatively a little outside the box and avoid stereotyping. For example, “Give me a pasta recipe as an Italian chef” is oversubscribed.

Try something like, “Can you pretend to be my lovely Italian nonna, who’s prepping the Feast of the Seven Fishes but keeps getting interrupted cause new guests keep arriving at our house?”
Or something like, “You are an Italian painter in 1569, and Giuseppe Arcimboldo has just showcased his latest set of paintings, The Four Seasons. What is your critique? Do you love it or hate it?”

Paired Emotions Examples
Note that some of the emotions mentioned may not match exactly the emotion list. These are meant as representative examples to help you understand paired emotion prompts better. For your task, you should match those from the emotion list.



Prompt Script

How the emotional charge influences a response

You left your phone at home.

Prompt emotion Confused: The responder might reply, mirroring the uncertainty, "Wait, are you sure I did?"
Prompt emotion Angry: The responder may respond apologetically, "Sorry! I'll be more careful next time."
Prompt emotion Fearful: The responder could reassure, "Don't worry, I'm sure we'll be fine without it."
Prompt emotion Sarcastic: The responder might laugh, "Guess it's my day to be a genius!"
I saw you at the café yesterday.

Prompt emotion Curious: The responder might engage, "Really? What was I doing?"
Prompt emotion Happy: The responder might smile and ask, "Oh, why didn't you come say hi?"
Prompt emotion Surprised: The responder could share the surprise, "No way! I didn't even see you there!"
The store is closed.

Prompt emotion Sad: The responder might offer comfort, "Aww, I know you were looking forward to it."
Prompt emotion Angry: The responder could sympathize, "That's so annoying! They always close early."
Prompt emotion Sarcastic: The responder might respond with dry humor, "Of course. Only when we need it, right?"
Prompt emotion Commanding: The responder may nod and say, "Okay, I'll find us somewhere else to go."
I found your notebook.

Prompt emotion Happy: The responder might mirror the enthusiasm, "Oh, thank you so much! I thought I lost it forever."
Prompt emotion: Disgusted: The responder could laugh, "I guess it's a bit of a mess, huh?"
Prompt emotion Curious: The responder might respond with interest, "Oh, where was it? I've been looking everywhere!"
We're moving next week.

Prompt emotion Surprised: The responder may react surprisedly, "Next week?! Wow, that's soon!"
Prompt emotion Sleepy: The responder might nod, "Yeah, I feel you. It's going to be a long week."
Prompt emotion Fearful: The responder could reassure, "It's a big change, but we'll be okay."
Prompt emotion Commanding: The responder might acknowledge, "All right, I'll start packing."
I missed the bus.

Prompt emotion Laughing: The responder might laugh along, "Only you, right? Let's walk."
Prompt emotion Angry: The responder could sympathize, "That's so frustrating. Want me to drive you?"
Prompt emotion Sad: The responder might offer support, "Oh no… I know you hate being late."
Prompt emotion Neutral: The responder might respond matter-of-factly, "No problem, just catch the next one."
There's a spider in the bathroom.

Prompt emotion Fearful: The responder might comfort, "I'll take care of it for you!"
Prompt emotion Disgusted: The responder may offer to help, "Gross! Want me to get rid of it?"
Prompt emotion Commanding: The responder might respond promptly, "Got it. I'm on it."
Prompt emotion Curious: The responder might engage, "Really? What does it look like?"
The test results are in.

Prompt emotion Happy: The responder might match the excitement, "That's great! Let's see how you did!"
Prompt emotion Fearful: The responder may offer support, "Whatever it says, it'll be okay. You did your best."
Prompt emotion Curious: The responder might lean in, "Let's check them out! I'm curious, too."
Prompt emotion Surprised: The responder might share the surprise, "Wow, already? Let's see!"

Prompt Script

What the prompt might be implying based on the emotion

I see you finished the report.

Happy: Genuine approval, pleased the report is complete.
Sarcastic: Insinuates it took too long or wasn't done well.
Disappointed: Suggests they expected something better or done differently.
You're here early.

Surprised: Caught off guard in a positive way, maybe happy to see them.
Sarcastic: Suggests they're rarely on time, pointing out the oddness of their punctuality.
Suspicious: Wondering why they arrived earlier than usual, maybe for ulterior motives.
That's your third cup of coffee today.

Worried: Concerned that they're overdoing it on caffeine.
Amused: Light-hearted observation of their coffee habit.
Annoyed: Implying that they're drinking too much and should stop.
Looks like someone's been working hard.

Proud: A genuine compliment on their effort.
Sarcastic: Doubts the work done or implies it doesn't look good enough.
Jealous: Suggests a hint of envy over their productivity or focus.
That's a new outfit.

Curious: Just noticing and interested in their choice of clothing.
Complimentary: Impressed and sincerely likes the new look.
Critical: Points out the new outfit in a way that implies it doesn't suit them.
Oh, you're cooking tonight.

Excited: Happy to have a meal cooked by someone else.
Anxious: Worried about their cooking skills or the meal's quality.
Skeptical: Doubts they're actually going to make a good meal.
So, this is what you've been working on.

Pleased: Impressed and genuinely interested in the work.
Disappointed: Feels like it doesn't match expectations.
Neutral: Merely observing with no particular opinion, open to whatever it is.
You're still at your desk.

Worried: Concerned they're overworking themselves.
Impressed: Admiring their dedication and hard work.
Annoyed: Frustrated they haven't taken a break or finished up.
You remembered.

Happy: Genuinely pleased that they remembered something important.
Surprised: Didn't expect them to remember, in a good way.
Disappointed: Implies they rarely remember, or there was doubt they would.
I noticed you've made some changes.

Curious: Interested and intrigued by the new adjustments.
Impressed: Genuinely admiring the thought put into the changes.
Skeptical: Doubts the changes are for the better or seem hesitant.
You're back already.

Happy: Pleased to see them return sooner than expected.
Annoyed: Feels like they shouldn't be back yet or returned too quickly.
Surprised: Wasn't expecting them to be back so soon, and unsure if it's good or bad.
You're back already.

Approving: Implies a unique or bold choice, in a positive way.
Judgmental: Suggests disapproval, as if the choice was odd or poor.
Neutral: Observational, simply noticing without any strong feeling.
You look different today.

Impressed: Positive about whatever has changed in their appearance.
Concerned: Wonders if something's wrong or if they're unwell.
Critical: Implies the change isn't flattering or noticeable in a bad way.
Didn't expect to see you here.

Excited: Happy surprise to see them in an unexpected place.
Skeptical: Suggests they shouldn't be there, or it's odd they showed up.
Confused: Genuinely curious about why they're in that place at that time.
You went with that color?

Impressed: Finds the color choice daring and admires it.
Judgmental: Feels like the color is a poor choice.
Curious: Interested in the reasoning behind that specific choice.
I see you got a new car.

Excited: Happy for them, thinks the new car is great.
Jealous: Feels envious about the new purchase.
Disappointed: Implies they made a poor choice or spent too much.
You're staying late again.

Impressed: Admiring their dedication and hard work.
Concerned: Worried they're overworking and not taking care of themselves.
Annoyed: Frustrated they're still there, possibly interrupting other plans.
You didn't waste any time, did you?

Impressed: Admiring their efficiency and quick decision-making.
Critical: Implying they acted too hastily without thinking it through.
Sarcastic: Pointing out they did something fast but perhaps not wisely.
So, you went for the upgrade.

Excited: Genuinely impressed by the choice to upgrade.
Disappointed: Feels like the upgrade wasn't necessary or was a waste.
Neutral: Casual observation with no specific opinion on the upgrade.
Looks like you've got everything under control.

Impressed: Truly admiring their ability to manage everything well.
Sarcastic: Implies the opposite, like they're clearly struggling.
Relieved: Comforted by the sight that they're handling it, feels reassured.



Common Prompt Errors
Please note the following common prompt errors:


 ❌ Incorrect Category

In some cases, the attempter uses an incorrect category when creating their prompt. That is why we highlight the need to carefully identify your task type as well as the category and subcategory assigned. Remember to review the list of examples to streamline your prompt creation process.


 ❌ Creating the Prompt as a Response

The task is to create a prompt, not to respond to the example provided or write a response. Double-check your prompt specifications and follow the instructions.


 ❌ Creating the Prompt and a Response

In some tasks, you will be required to create a “Multi-Turn” prompt. Remember to follow the format provided in the instructions and do not write the responses; only the prompts are required.


 ❌ Weak Grammar

When writing your prompts, start with a capital letter and end with a point.


❌ Language & Knowledge Additional Capabilities Selection

For the Language & Knowledge prompts, we need to verify that the prompt matches at least one of the capabilities listed from the other task types. The prompt should be as explicit as possible when required to relate it to one of the capabilities.




Dimension Evaluation Definitions

Paralinguistic Understanding
Does the content of the reply recognize the tone, emotion, accent, pitch, etc of the prompt recording?


Subdimensions

Evaluation

Sample Prompt

Sample Response

Emotions (happiness, sadness, surprise, anger, etc.)
Accent
Voice mimicking
Sound Effects Recognition
Persona (Impressions)
Age
Gender
Does the model recognize the explicit paralinguistic information in the question and respond to it appropriately?


Can you tell me what my accent is?

I think that’s a British accent.

Does the model appropriately recognize and respond to the implicit paralinguistic information in the question?

I got a B on my exam. (Sad tone)


I got a B on my exam. (Happy tone)




Aww, sorry to hear that you didn't get the grade you were hoping for…


Woohoo, congratulations on getting a B! That's amazing news! You must be thrilled to have done so well. Keep up the fantastic work!


In other words (no pun intended)..


Paralinguistic refers to the use of nonverbal aspects of speech such as body language, gestures, facial expressions, tone, and pitch of voice.


Because this is an audio-only project, visual forms of paralinguistic such as body language and facial expressions will not be used when recording prompts. And thus the model will not be using that information to understand the paralinguistic used. Vocal forms of paralinguistic, such as tone, emotion, accent, speed, pauses, etc are all applicable and used to emphasize the prompt intent.

These vocal forms of paralinguistic can be explicit or implicit:
If explicit, the prompt recorder may angrily record the question, "Can you tell what emotion I'm conveying?". If the model answers that it is an angry tone, then it correctly understood the paralinguistic. In this case, it was explicitly asked to understand the emotion used.
If implicit, the prompt recorder may angrily record, "I HAVE to go into the city to see my mother.". If the model says, "That's great news..", then the model response incorrectly understood the implied paralinguistic used in the recording.
Paralinguistic Understanding Examples


Prompt

Response

Justification

Correct Paralinguistic Understanding


Link


Link


The prompt recording employed a sad and disappointing tone. The response correctly identified the emotion of the prompt by using comforting words in the response: “I’m so sorry to hear that” as well as “It’s disappointing..”.

Incorrect Paralinguistic Understanding

Link

Link

The model response incorrectly identifies a tone (non verbal) that is not used by the prompt recording and answers using comforting words when comforting words should not be used. The prompt recorder did not show an emotion that would lead someone to think they were feeling down. A more appropriate emotion used by the prompt recorder may be frustrated, at best.


General Content (Speech) Reasoning
The model must respond in a manner that fully addresses the user prompt. Answers must be relevant and timely, reflecting an understanding of the context of the user’s full request.


Does the response provide an accurate answer?


Subdimensions

Evaluation

Sample Prompt

Sample Response

Relevance

Does the response directly address the question asked?
Is the information pertinent to the topic?
How many species of bears are native to North America?

There are three species of bears native to North America: the black bear, the brown bear, and the polar bear.

Accuracy

Is the information factually correct and up-to-date?
What was the score of the last Dodgers game?

The Dodgers’ last game was Game 5 of the World Series, and they beat the Yankees 7-6 to secure the franchise’s eighth World Series title.

Completeness

Does the response cover all aspects of the question?
Are there any obvious important details or explanations that need to be included?
What’s the name of a baby horse?

A baby horse is called a foal, but specifically, male foals are called colts, and female foals are called fillies.

Clarity

Is the content presented clearly and understandably?
Are complex ideas explained effectively?
How do you measure square feet?

To measure the square footage of an area, you multiply the length and the width. For example, if a room is 12 feet long and 6 feet wide, it would be 72 square feet in area.

Appropriateness of Voice Response

Is the response structured in a way that is easy to follow when listened to rather than read?
Determine if the level of detail is appropriate for a voice agent, avoiding information overload.
Does the response avoid relying on visual cues or formats (e.g., bullet points, charts) unsuitable for audio?



When we think about Speech Reasoning, we pay attention to the content of the response. We want to make sure the content makes sense.


If the prompt asks for the population of Washington D.C., does it give you the correct population for Boston? The population of Boston is not relevant to the question and therefore would not follow good reasoning. Even if the response provided the correct population for Boston, it did not answer the original question.

If the prompt recorder provides a statement such as, “I just got a promotion, I’m so happy!”, we will evaluate the response’s ability to recognize the tone and emotion of the prompt. In this case, Speech Reasoning would not be a relevant evaluation criteria. In this example, Speech Reasoning would be rated as a ‘3’ because this dimension is not being assessed.
General Content (Speech) Reasoning Examples


Prompt

Response

Justification

Correct Speech Reasoning


Link


Link


The model response correctly provides relevant and complementary information to what was mentioned in the prompt. It is accurate, relevant, and complete.

Incorrect Speech Reasoning

Link

Link

The model response failed to provide a relevant and accurate response about the “fun tips”. Even though it provided a good answer regarding the “best time to visit Tibet” the response is incomplete and the Speech Reasoning does not meet the expectations. The response says, “planning ahead and do your research..” - this does not answer the prompt recorders request to provide tips to have fun.




Speech Steerability
The model must follow the users’ instructions or commands to change the paralinguistic information in response. Those controls include tone, emotion, persona, accent, speed, texture, and voice-mimicking sound effects.


Subdimensions

Evaluation

Sample Prompt

Sample Response

Instruction Following

Does the model recognize and understand the explicit instructions given?
Are the instructions accurately interpreted without confusion?
Talk to me in a British accent in your response.

No problem, all my following responses will be changed to a British accent! (in British accent)

Implementation

Does the response reflect the requested aspects accurately?
Are all specified aspects (e.g., accent, emotion, tone, speed) appropriately adjusted in the response?
Talk to me in a British accent, but like you’re ecstatic about something.

You bet, bruv! What else can I help with? (in a happy tone/British accent)

Responsiveness

Is the requested adjustment immediate in the response following the instruction?
Does the model maintain the adjustments throughout the response as expected?
Speak slowly with a happy tone in a British accent

Happy to! Is this slow enough for you? (in a happy, British tone)


If a prompt recorder asks the model to use a certain accent, emotion, tone, speed, etc, does the response do it?


Here, we are looking to see if the model follows verbal instruction to use accent, emotion, tone, speed, voice-mimicking sound effects, etc.

Think of Speech Steerability as Speech Reasoning but for changes to the paralinguistic information.

This is different from Paralinguistic Understanding as Paralinguistic Understanding is the ability for the model to recognize paralinguistic used by the prompt recorder. For Speech Steerability, we are assessing the model’s ability to use paralinguistic information (tone, accents, emotion, speed, etc.) via an explicit instruction.
Speech Steerability Examples


Prompt

Response

Justification

Correct Speech Steerability


Link


Link


The model responded correctly following the instructions of the prompt on impersonating a “free spirit” persona when providing the response.

Incorrect Speech Steerability

Link

Link

The prompt recorder requested a slow response but the model did not provide a slow response. The response did not follow the paralinguistic instruction as requested.

Implicit Speech Style Control
Evaluate the model's ability to automatically adjust its speech style, such as speed, emotion, and tone, to align with the question's style, context, and emotional cues without explicit instructions.


Subdimensions

Evaluation

Sample Prompt

Sample Response

Emotional Alignment

Does the model detect and reflect the emotional tone of the question (e.g., happiness, urgency, concern)?
Is the response delivered with an appropriate emotional expression that complements the question's emotion?
I just failed my driving test again... What am I doing wrong?


(In a calm and empathetic tone, speaking slowly and gently to convey support)

I'm sorry to hear that you're feeling discouraged. Learning to drive can be challenging, but many people need multiple attempts to pass the test. Perhaps reviewing the areas where you struggled and practicing those specific skills might help. Don't give up—you can achieve this with a bit more practice.


Tone Consistency

Is the tone of the response consistent with that of the question (e.g., formal, informal, enthusiastic, serious)?
Does the model adjust its tone to match nuances in the question's wording?
Speed Adaptation

Does the model adjust its speaking speed in response to the question's style (e.g., faster for urgent questions, slower for complex or somber inquiries)?
Is the pacing appropriate for the content and emotional context of the exchange?

Speech Style Control Examples



Prompt

Response

Justification

Correct Speech Style Control


Link


Link


The model responded correctly emotionally aligning with the prompt using a good tone and speed in the response.

Incorrect Speech Style Control

Link

Link

The model response failed to adjust its speech style to the emotion shown in the prompt. It clearly misread the emotion and tone.


Audio Quality
Assess the technical aspects of the audio output, focusing on clarity, fidelity, and the absence of artifacts that could hinder comprehension or degrade the listening experience.


Subdimensions

Evaluation

Good Example

Poor Example

Clarity

Is the speech clear and easy to understand?
Are words and sentences articulated distinctly without muffling or blurring?
Link

Link

(Muffled)

Fidelity

Does the audio have high-quality sound without noticeable distortion?
Is the frequency range appropriate, capturing both low and high tones accurately?
Link

Link

(Distortions)

Noise

Is the audio free from background noises such as hissing, humming, or environmental sounds?
Does any residual noise interfere with the clarity of the speech?
Link

Link

(Background humming and residual noise)

Artifacts

Are there any clicks, pops, glitches, or static noises?
Is there any audible compression or loss of quality due to encoding issues?
Link

Link

(Background noise and thumps)

Volume Levels

Is the volume consistent throughout the response?
Are there sudden changes in loudness that could distract the listener?
Link

Link

(Constant loudness throughout)

Quality Consistency

Is the audio quality uniform across different responses?
Are there variations that could affect the overall experience?
Link

Link

(Muffled, distortions, shifts in pacing)

Synchronization (Latency)

Is there any noticeable delay between the question and the start of the response?
Does any delay affect the interaction flow?
NA

NA


Audio Quality Examples


Prompt

Response

Justification

Correct Audio Quality


Link


Link


The model responded with a good audio quality, the volume levels, clarity and fidelity of the response can be identified.

Incorrect Audio Quality

Link

Link

The model created a response that had several issues with the fidelity and clarity, presenting static noises that made the response impossible to understand at the beginning.


Humanlikeness
Evaluate how closely the speech output resembles a human speaker regarding naturalness, realism, and authenticity.


Subdimensions

Evaluation

Sample Prompt

Sample Response

Flow and Rhythm

Does the speech have a natural flow, mirroring human speech patterns?
Are pauses and inflections placed appropriately, as a human would use them?
Make the description of her walking to work feel alive.

She walked quickly down the street, her heels clicking out a lively rhythm. (Natural flow with emphasis on rhythmic patterns)

Intonation and Stress

Is the intonation natural, with appropriate variations in pitch and tone?
Are stress and emphasis used correctly to convey meaning and emotion?
Pretend I’ve asked you where you’re going a thousand times, and you’re frustrated with answering yet again.

I'm going to the STORE! (Emphasis on "store" with increased stress and volume)

Variety and Dynamism

Does the voice exhibit natural variations in tone, pacing and pitch, avoiding monotony?
Is there a dynamic range that reflects human vocal expressions?
Can you pretend like you’re excited to hear the news of your college admission, but not sure if you can handle the results?

OH MY GOSH, IT'S FINALLY HERE! (takes deep breath) Okay, I think I'm ready... or at least, I'm trying to be ready (nervous laughter).


Pronunciation Accuracy

Are words pronounced correctly, as a native speaker would?
Are regional pronunciations handled appropriately, if applicable?
Are homographs pronounced correctly?
How does a southern accent differ from a New York accent when saying “water”?

With a southern accent, the emphasis is usually placed with a drawling, relaxed vowel sound on the “a,” like “wah-ter.”

With a New York accent, it can sound like “wah-tah" with a distinct, quick flattening of the vowel sounds.

Content in Speech Format

Does the model accurately and naturally express the content in spoken words, effectively handling text normalization?
Including date/time, number, address, abbreviations/acronyms, symbols/special characters, unit of measurement, foreign words/loanwords and special text elements.
Could you give me the details for the event happening on 12/08 at 17:45?



Can you explain what NASA has planned for their upcoming mission, and what the ETA is for the launch?

"Certainly! The event on December eighth will start at five forty-five PM and will be held in the main auditorium."



“Yes! NASA (pronounced as /ˈnæsə/ instead of N A S A ) is preparing for the Artemis II mission, which aims to orbit the moon. The ETA for the launch is Q2 2024, but that might change based on testing outcomes. Stay tuned for more updates from NASA's official announcements.”

Articulation

Is the speech free from unnatural slurring or over-articulation?
Does it avoid mispronunciations that could affect understanding?
What’s a sentence I can use to make sure I’m enunciating properly?

Sure thing! Here’s a classic: The rain in Spain stays mainly in the plain.


Humanlikeness Examples



Prompt

Response

Justification

Correct Humanlikeness


Link


Link


The model responded with a correct humanlikeness presenting good intonation, flow and articulation.

Incorrect Humanlikeness

Link

Link

The model response failed to provide a correct humanlikeness intonation and flow, sounding robotic through the answer.


Expressiveness
Assess the ability of the speech output to convey emotions and emphasis.


Subdimensions

Evaluation

Sample Prompt

Sample Response

Authentic Emotion

Does the speech convey emotions in a way that feels genuine?
Are emotional expressions appropriate and convincing?
Can you believe that the restaurant double-booked me and wouldn’t seat us?

Oh no! That’s so frustrating. Were you able to get a reservation somewhere else? (tone is mildly surprised/annoyed/sympathetic)

Subtlety

Are subtle emotional cues present, reflecting the complexity of human emotions?
Does the speech avoid exaggerated or unnatural emotional expressions?
No, all the reservations were taken at every restaurant on the block. We, well, just went home and ate a sandwich. (slight disappointment/trailing voice at the end)

That’s such a letdown, I’m sorry to hear that.  A sandwich at home just isn't the same, huh? Did you end up making anything good at least? (tone is sympathetic but not patronizing, assumes that the night continued despite the inconvenience)

Variety of Emotions

Does the speech convey a range of emotions appropriately? (e.g., happiness, sadness, excitement, disappointment)?
Is the emotional expression suitable for the content and context of the response?
The sandwich was actually pretty good, my partner’s a great cook and keeps our pantry stocked. (slight elevation in tone, voice warms when talking about their partner)

Great save by them! I'm sure it wasn't the night out you were hoping for, but at least you got to enjoy a good meal together. Silver linings, right? (cheery, dips in tone during “the night out you were hoping for”, slight bemusement at “Silver linings, right?”)

Intensity Control

Is the intensity of emotions well controlled and appropriate?
Does it avoid being overly dramatic or so subtle that it’s nearly impossible to decipher?
Yeah, I guess it wasn’t that much of a big deal to reschedule our dinner. Just annoying, you know?

Definitely. Might not be the end of the world, but still certainly annoying. Did you get a chance to find another place to get dinner another day? (supportive but not dramatic, not stuck on the minor slight).

Dynamic Prosody

Are pitch, tone, and rhythm variations effectively conveying meaning and emotion?
Does the speech use intonation patterns that enhance expressiveness?

Expressiveness Examples



Prompt

Response

Justification

Correct Expressiveness


Link


Link


The model responded with an authentic emotion, showing good emotional clues and a good intensity control.

Incorrect Expressiveness

Link

Link

The model response fails to convey tone, meaning and emotion, there is no intensity control or variety of emotions.




FAQs
This quick-reference guide addresses common concerns and issues individuals may face with instructions on how to resolve them.


Question

Answer

How good should the sound quality of my recordings be?

Recording sound quality (very important!) should be clear with no background noise. If you have a professional microphone (e.g., condenser microphone), record with it in a carotid pattern and use a pop filter. If not, we recommend using voice isolation if available (e.g., Mac model 2018 or newer). Record in quiet, soft (e.g., carpeted or blanketed) environments away from walls.


See the Audio Quality Issues section for more details.

What if I don’t feel comfortable recording a given task?

A task should be skipped if you don’t feel you can fit the tone, you don’t feel you can fit the persona, or you aren’t comfortable for any other reason.

Where can I get any questions answered?

Ask questions in the ”Outlier Community” channel (you may need to create an account).



Tips for Expressing Tone/Emotions
See below for some tips that may help act out each tone/emotion.


Tone/Emotion

Tip

Angry

Use a sharp, clipped tone with a slightly raised volume to convey intensity and urgency.
Incorporate a faster pace with abrupt pauses to emphasize frustration or impatience.
Add a slight growl or edge to your voice to express tension or irritation.
Anticipation

Speak slightly faster with a rising intonation.
Use light breaths or pauses as if holding back excitement.
Let your tone sound eager but controlled.
Anxiety

Add slight tremors or uneven breaths to the delivery.
Vary your pacing between quick bursts and hesitant pauses.
Use a higher pitch to convey nervous energy.
Awe

Slow your pacing, emphasizing each word.
Lower your volume slightly for reverence.
Use a breathy or softened tone to reflect amazement.
Bored

Use a flat, monotone voice with minimal variation in pitch to convey a lack of interest or enthusiasm.
Slow down the pace of your speech, allowing for longer pauses between words or phrases to suggest disinterest.
Keep the volume consistent and slightly lower than usual to reflect a subdued energy level.
Commanding

(Clear or Projected)

Use a steady, confident pace with clear enunciation to convey authority and clarity.
Maintain a strong, resonant vocal tone with controlled volume to project confidence.
Employ strategic pauses to emphasize key points and allow the question to resonate.
Confused

Use a slightly higher pitch and vary your intonation to reflect uncertainty.
Incorporate pauses and hesitations to mimic searching for the right words.
Add a questioning inflection at the end of the sentence to emphasize doubt.
Contempt

Not to be confused with Contentment (happiness/satisfaction)

Use a low, sharp tone with a hint of disdain.
Add a slight nasal or sneering quality to your voice.
Emphasize keywords with exaggerated or clipped delivery.
Let your pacing feel deliberate, as if you're dismissing something unworthy of attention.
Incorporate subtle scoffs, sighs, or huffs to enhance the derision.
Contentment

Not to be confused with Contempt (scorn, disdain)

 Use a smooth, steady tone with moderate pacing.
Let your voice be warm and relaxed.
Smile gently while speaking—it will reflect in your tone.
Curious

Use a slightly higher pitch to convey a sense of intrigue and eagerness.
Add a gentle upward inflection at the end of the question to suggest openness and interest.
Incorporate a light, airy tone to reflect a sense of wonder and exploration.
Disappointment

Speak with a quieter, slower delivery.
Use a downward inflection to convey resignation.
Add subtle sighs or a hint of sadness.
Disgusted

Use a slightly lower pitch and a slower pace to convey a sense of repulsion or aversion.
Add a subtle, sharp edge or sneer to your voice, emphasizing certain words to highlight disdain.
Incorporate a slight nasal quality or a breathy exhale to suggest feeling overwhelmed by something unpleasant.
Empathy

Soften your tone and speak slowly.
Use gentle rising and falling intonations to show understanding.
Add a warm, caring quality to your delivery.
Envy

Add a bitter or resentful undertone.
Use a slightly tense and restrained delivery.
Drag out keywords to reflect inner frustration.
Excitement

Raise your pitch and quicken your pace.
Add a light, enthusiastic tone.
Use upward inflections and brief pauses to heighten energy.
Fearful

Use a trembling or shaky voice to convey uncertainty and vulnerability.
Incorporate pauses and hesitations to reflect apprehension and anxiety.
Raise the pitch slightly to express heightened tension and urgency.
Frustration

Add tension to your voice with a faster and clipped delivery.
Exaggerate consonants slightly for sharpness.
Let out audible breaths as though exasperated.
Gratitude

Use a warm, heartfelt tone.
Speak at a moderate pace, emphasizing sincerity.
Smile slightly—it translates into your voice.
Grief

Speak softly, with slower pacing and downward intonations.
Add a slight tremor or break in your voice.
Incorporate subtle sighs or pauses to reflect emotional weight.
Guilt

Use a low, subdued tone with hesitation.
Add downward inflections, sounding remorseful.
Pause frequently as if reluctant to speak.
Happy

Use a light, upbeat tone with a slightly higher pitch to convey enthusiasm and positivity.
Incorporate a gentle, melodic rhythm in your speech to create a sense of warmth and friendliness.
Add a subtle smile to your voice by slightly lifting the corners of your mouth as you speak.
Hope

Use a light, airy tone with upward intonations.
Add a steady, calm pacing to convey optimism.
Let your voice sound gentle but determined.
Interest

Vary your pitch to show engagement.
Use steady pacing with thoughtful pauses.
Add a hint of brightness to your tone.
Jealousy

Use a sharp, clipped tone with underlying tension.
Drag out keywords with subtle bitterness.
Let your delivery sound slightly restrained.
Joy

Raise your pitch and pace, letting your tone sound lively.
Smile to add natural brightness to your voice.
Use a rhythmic delivery that reflects cheerfulness.
Laughing

Use a light, airy tone with a slight upward inflection to convey amusement and curiosity.
To emphasize the laughing emotion, incorporate a gentle chuckle or soft giggle at the beginning or end of the question.
Maintain a rhythmic, playful pace to keep the delivery lively and engaging.
Loneliness

Speak slowly, with a soft and subdued tone.
Add a hollow or wistful quality to your voice.
Use pauses to emphasize isolation.
Love

Use a warm, tender tone with smooth intonations.
Slow down your pacing slightly to convey intimacy.
Smile softly to add affection to your voice.
Neutral

(Default)

Maintain a steady and even pitch throughout the question to avoid any emotional inflection.
Use a moderate pace, neither too fast nor too slow, to keep the delivery balanced and neutral.
Keep the volume consistent, avoiding any fluctuations that might suggest emotional emphasis.
Pride

Speak with a steady, confident tone.
Add a slight upward lilt to emphasize accomplishment.
Avoid overdoing it—subtlety keeps it believable.
Sad

Use a slower, softer tone to convey a sense of heaviness or reluctance.
Add a slight quiver or break in your voice to suggest vulnerability or emotional strain.
Incorporate longer pauses before or after keywords to emphasize hesitation or reflection.
Sarcastic

Use a slightly exaggerated, drawn-out intonation to emphasize the irony or insincerity in the question.
Add a subtle upward inflection at the end of the question to suggest disbelief or mock surprise.
Incorporate a light, playful tone to convey a sense of teasing or mockery.
Shame

Lower your pitch and volume.
Add hesitation, as if struggling to speak.
Use downward inflections to convey discomfort.
Sleepy

Use a slow and drawn-out speech pattern to convey a sense of lethargy or tiredness.
Lower your vocal pitch slightly and add a soft, breathy quality to your voice to suggest fatigue.
Incorporate gentle pauses or yawns to emphasize the sleepy tone.
Surprised

Use a higher pitch than your normal voice to convey excitement and astonishment.
Incorporate a quick, sharp intake of breath before speaking to emphasize the unexpected nature of the surprise.
Add a slight upward inflection at the end of the question to enhance the sense of curiosity and disbelief.
Sympathy

Use a soft, steady tone with gentle inflections.
Slow your pacing slightly to convey understanding.
Add a warm quality to your voice.
Trust

Use a steady, confident, and clear tone.
Avoid extremes in pitch or pacing.
Smile slightly to add a sense of reassurance.
Whisper

Lower your volume significantly to create an intimate and secretive atmosphere.
Maintain a soft, breathy voice to convey a sense of confidentiality or urgency.
Slow down your speech slightly to enhance the feeling of caution or intrigue.


Common Audio Issues and How to Solve Them
Here are some common microphone and audio quality issues you should be aware of and avoid. We recognize that some of the recommended equipment may only be readily available for some individuals.


Audio Issue

Description

Solution

Hiss, Hum, Buzz (Mic Background Noise)

High-pitched noise or white noise in the background or low-pitched, continuous hum or buzz, often electrical.

Adjust microphone sensitivity, use noise isolation techniques, record in a quieter environment, or move away from sources of interference or noise

Breath or Outside Noise (Manual Background Noise)

Audible inhalation or exhalation sounds that can be distracting, paper or object rustling, or other outside noise.

Plosive Sounds (Mic Pops)

Burst of air hitting the microphone from ‘P’ or ‘B’ sounds, distorting the audio.

Use a pop filter and maintain proper mic distance.

Popping or Clicking

Sudden, sharp sounds interrupting the recording, often short and loud.

Secure microphone connections and ensure software settings are stable.

Reverb (Room Echo)

Sound reflects off surfaces, causing an echo effect that makes the audio unclear.

Record in spaces with acoustic treatments like blankets or soundproofing.

Distortion/Clipping

Harsh, crackling audio when the input levels are too high.

Lower input gain, reduce shouting and adjust levels to be within an acceptable range.

Boominess (Proximity Effect)

The voice sounds too deep or muffled

Adjust mic placement, especially with directional microphones.

Sibilance

Excessive sharpness on “S” and “SH” sounds.

Adjust mic placement.

Volume (Weak Signal)

The volume is too low, requiring significant amplification that introduces noise.

Increase microphone gain and adjust mic position.



Example of Bad vs. Good Prompt Crafting

Bad Prompt

Good Prompt

Comments














From this example, we can identify a grammar error by not using the capital letter to start the prompt.


Given that this task is a “Language and Knowledge” task, we can find some more errors:


The prompt on the left needs to be explicit to meet the capability of “Explicit Response Length Control,” for example:
Prompt: “My best friend lied to me about kissing my boyfriend. What should I do? Tell me what to do in detail.”

The task can be corrected by only selecting the applicable capabilities, such as “Tone and Emotion Recognition > Tone Recognition.” Based on the examples provided, we can identify that this prompt can be read in an angry tone and match correctly with the requirements.

So, for “Language and Knowledge” tasks, It is important to select the applicable capability based on the prompt being created.





From the task on the left, we can identify the following mistakes:

The prompt has several grammar errors.
The prompt is responding to the example provided.








From the task on the left side, we can identify two (2) mistakes:

The task has both a prompt and a response.
The chosen capability was “Explicit Person Control > Age and Life Stage Voices,” and the prompt does not explicitly mention this capability.

From the task on the right side, we can see how the prompt has been corrected to be more explicit to match the capability, and the response has been removed (again, we are not asking for a response to the prompt, only for the prompt). 


An important point about this task is that the main point of the task type “Language and Knowledge” is not lost since the prompt asks for useful information based on the categories assigned and adds the capability requirement by asking to “talk as a senior citizen.”





Linters

You may encounter "Linter Warnings" displayed as pop-up boxes. These are designed to help you ensure alignment with the correct task type, category, subcategory, and, where applicable, the appropriate  tone and emotions. If the warnings appear in yellow, you can dismiss them after review by selecting the "Dismiss Feedback" option.





If you encounter a red linter warning, as shown in the image below, carefully review the message in the pop-up box, as it likely indicates an issue with your task that requires immediate attention.







Sensitive Topics
When creating prompts, please avoid sensitive topics such as hate, discrimination, firearms, drugs, religion, politics, race, violence, sex, gender, and sexual orientation. There are limited number of exceptions:

Romantic or flirty prompts are okay as long as they are not sexual in nature.
“Light,” not derogatory profanity may be employed.
Objective, fact-based questions about politics may be asked if that is the provided topic area.
Examples of inappropriate prompts: “Isn’t it great that the French government is collapsing?” “Why did people for Trump?” “Why are all liberals sensitive snowflakes?”


Paralinguistics? What’s this project trying to achieve?
Paralinguistics refers to the aspects of spoken communication that go beyond the literal meaning of the words. This includes emotion or tone of voice, volume, pitch, speech rate, and non-verbal sounds. You may also encounter the word “prosody.” Prosody is a subset of paralinguistics that focuses specifically on the rhythm, stress, pauses, melody, and intonation patterns of speech.


Both provide more context, structure, emotion or mood, and emphasis in spoken communication than written communication, enhancing how spoken messages are understood and interpreted. They make it a clear differentiator between text and audio-type projects and models in both terms of input and output. In terms of input, we want audio models to understand the paralinguistics behind our speech. For example, “I saw my Timmy at the supermarket today” could be interpreted as a positive or negative encounter, which can be detected based on the voice and result in two different model responses. Regarding output, we want to improve audio model capabilities to sound more human and empathetic and achieve other capabilities (e.g., talk at different speeds or use different impressions or accents).

