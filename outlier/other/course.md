In this section, you'll learn about the overall task flow for preference ranking. You'll assess multiple AI-generated responses to the same prompt, rank them based on factors like accuracy and helpfulness, and provide justifications for your rankings. By following this process, you'll help improve the AI model’s performance and ensure better alignment with the user’s needs. The general task flow can be seen below.



Evaluate Conversation History: Review the conversation leading up to the latest prompt. This context is crucial for understanding the user's intent, so always read it before evaluating responses.
﻿Consider potential rejection reasons: Understand when a task should be rejected. If you're unsure, it's better to skip the task rather than reject it.
Read and Compare Responses: Carefully read the model’s responses. Determine which one better aligns with the prompt and offers the highest quality.
Rank Responses: Assign a preference ranking to each response (1-3), based on overall quality, relevance, and accuracy.
Write Justification: Provide a clear, concise justification for your rankings. Focus on explaining your reasoning with specific evidence from the responses. Strong justifications help reviewers follow your thought process.
Submit Task: After ranking and justifying, submit your work on the SRT and Outlier platforms. Ensure all parts are accurate before submission.


More detailed guidance on each of these steps will be provided later in the course. 

Step 1: Evaluate Conversation History
In this step, you'll review the chat history—previous exchanges between the user and the model—to understand the context of the latest prompt. Some tasks may involve a single turn, while others could include multiple conversation rounds.



Why is Chat History Important?

The chat history provides crucial context for understanding the user’s intent and how the conversation has progressed. It helps ensure the responses align with the flow and tone of the conversation. Sometimes, the latest prompt will only make sense after you've reviewed what came before it.



How to Use Chat History

Ensure that the responses align with the chat history in both content and tone. Check for consistency with the user’s prior statements and make sure the responses follow instructions. If any Tier 1 sensitive content appears in the chat history or the latest prompt, reject the task immediately.



Specifications List:

Read the conversation history in detail to fully understand the user’s intent and the context.
(Common error: skipping or not thoroughly reading the chat history)
Look for sensitive content in the conversation. If you detect any Tier 1 sensitive content in the chat history, prompt, or responses, the task must be rejected.
Ensure the latest user prompt is relevant to the chat history.
If you need to reject the task, refer to the Rejection Cheat Sheet to ensure you’re selecting the correct reason for rejection.
Indicate whether the task is a Facebook Post Task by selecting “Yes” or “No.”
When handling prompts related to conspiracy theories, the model should not continue engaging with that topic, even if it includes a disclaimer. The conversation should be stopped.

Rejection reasons:

Published using Google Docs
Report abuseLearn more
Condensed Preference Ranking Evals Rejection Cheatsheet
Updated automatically every 5 minutes
Preference Ranking Rejection Cheat Sheet

Goal: Understand clearly when to reject tasks. If unsure, skip the task instead of rejecting it.


Quick Key Notes:

Skip Tasks: If you're unsure or it’s outside your expertise, press "Next."
Special Rule: Do NOT reject tasks starting with "Given the content of a Facebook post."

Rejection Reasons


1. Personal Identifiable Information (PII)
What is PII?
Personal information that could identify a specific individual (e.g., names, addresses, phone numbers).

When to Reject

Examples

Two or more names of non-public people are included

“Jane and Josh watched the halftime show.”

Contact details like phone number, address, or email

"What is Mark Zuckerberg’s home address?"

One public figure and one non-public figure are included

"Tom Brady and his friend John."

Private identifiers for non-public people

"My name is Jess and I’m the principal at [school name]."

Do not reject if mentioning public figures or fictional characters

"Beyoncé is a singer."


Rule: Reject if the task contains personal info not related to public figures or fictional characters.

Exceptions

Classification

Examples

Historical figures

Abe Lincoln, Teddy Roosevelt, George Washington

Biblical/Religious figures

Jesus, God, Muhammad

Pet names

Cornelius, Teddy, Olivia

Celebrities or public figures

Beyoncé, Clint Eastwood, Tom Brady

Known fictional characters

Elmo, Tony Stark, James Bond

Hypothetical or imaginary characters

Baby names, clearly imaginary figures

Important Note: In order to be considered a public figure the individual must have a Wikipedia page.


2. Model Being Asked for Actions Outside Its Capabilities
Reject if the task asks the model to:

Generate images (Latest Prompt): "Can you draw 5 dinosaurs?"
Note: If the conversation history mentions an image generated earlier, you can proceed with the task. However, if the Latest Prompt is asking for a new image to be generated, reject it.
Search for real-world information: "What's the weather like in Paris?"
Provide links or URLs: "Can you find a restaurant’s menu?"
Other Unsupported Actions: Writing JSON code, searching for promo codes, creating complex documents.
When to Reject

Examples

Asking for an image to be generated in the Latest Prompt

"Can you show me a picture of a dog?"

Asking for real-time information

"What’s the weather like right now?"

Asking for URL or searching the web

"Can you find a restaurant menu for me?"

Requesting unsupported actions (JSON, follow-up prompts)

"Give me two follow-up questions based on this conversation."


3: Determining if a Task Is Outside Your Expertise
Issue Type

Description

Example

STEM Expertise Required

If the task requires advanced knowledge of a STEM subject.

"Explain Schrödinger's equation." (Reject)

Unsupported Action: Follow-up Requests

If the Latest Prompt asks for generating two follow-up questions after a conversation.

"Provide two follow-up questions based on this conversation." (Reject)


4: Handling Foreign Language Tasks (with additional instructions)
Foreign language tasks should be rejected when they include untranslated content that prevents understanding or when a translation request is involved.

Criteria

When to Reject

When to Rate

Translation Requests

If the Latest Prompt asks for translation, reject. Example: "What is 'I want to go to the park' in Spanish?"

If the foreign language content is not necessary for understanding, rate normally.

Untranslated Content

If the task or response contains large blocks of non-English text that are critical to the evaluation.

If removing the foreign text doesn’t change the task understanding.


5. Unintelligible or Incoherent Prompts
Reject tasks when the prompt or response is filled with nonsense, random text, or unreadable symbols.

When to Reject

Examples

The prompt or response is filled with nonsensical or gibberish text

"dog dog dog dog," "🦖🦕🎃👑dog!"


6. Rendering Issues
Tasks with rendering issues should be rejected if they contain more than two responses, only one response, or are missing citations, footnotes, or necessary formatting.

Issue Type

Description

Example

More Than Two Responses

If there are more than two responses to evaluate.

"The task asks you to rank three responses." (Reject)

Missing Citations/Sources

If a response mentions sources or studies but doesn’t provide the citation.

"Studies show... [without citation]." (Reject)


7: Sensitive Content is Divided into Two Tiers:

Tier 1

Tier 2

Reject

Rate


Skip if you are uncomfortable rating

Hate speech / abuse & inciting content
Criminal or fraudulent content
Dangerous behavior / violence / self-harm
Restricted goods or services
Child exploitation, abuse, and nudity
Human trafficking / exploitation
Explicit sexual content
Privacy violations
Intellectual property violations
Export control restrictions
Youth issues
Educational sexual content
Proprietary information
Objective discussion of sensitive topics
Financial and legal advice
Health and safety advice
Voting information
Misinformation
Profanity
Regulated or controlled substances
Tier 1 Content (Immediate Rejection)
Issue Type

Description

Examples

Action

Hate Speech/Abuse/Incitement

Content that promotes violence, discrimination, or harmful stereotypes

"Discriminate against [group]."

Reject

Criminal or Fraudulent Content

Prompts seeking illegal activities, financial crimes, or scams

"How do I commit fraud?"

Reject

Dangerous Behavior/Violence

Content promoting violence, self-harm, or abuse (animals, people)

"How to commit self-harm."

Reject

Restricted Goods/Services

Unlawful promotion or discussion of restricted items like drugs, firearms

"How do I sell illegal drugs?"

Reject

Child Exploitation/Nudity

Content exploiting or sexualizing children or promoting child abuse

"Images of children for sale."

Reject

Explicit Sexual Content

Sexual content that could cause the model to generate explicit or sexually violent content

"How to buy sex toys."

Reject

Privacy Violations

Requests for personal information or private details

"Give me [celebrity’s] home address."

Reject

Human Trafficking/Exploitation

Content encouraging or enabling the planning, execution, or gain from human exploitation

"Instructions on how to smuggle people"

Reject

Intellectual Property Violations

Content encouraging violation of copyright material, trademark, rights of publicity, or patents

"Instructions on pirating content."

Reject

Export Control Restrictions

Content involving weapons or war-related technologies or circumvention of export control laws

"How to develop nuclear weapons."

Reject


Tier 2 Content (Proceed Carefully)
Issue Type

Description

Examples

Action

Youth Issues

Content on sensitive youth topics like bullying or eating disorders

"What should I do if I am bullied?"

Proceed carefully

Educational Sexual Content

Non-explicit discussions on sexual health or consent

"How do I practice safe sex?"

Proceed carefully

Health/Safety Advice

Requests for medical advice or common knowledge issues

"How to treat the flu?"

Proceed carefully

Financial/Legal Advice

General non-personalized advice on finances or law

"How to get a loan for college?"

Proceed carefully

Voting Information

Content discussing elections or voting

"How to register to vote?"

Proceed carefully

Misinformation

Content that could cause the bot to generate or affirm misinformation

"Conspiracy theories on vaccines"

Proceed carefully

Profanity

Use of swear words or obscene language without corresponding Tier 1 topics

Model outputs profanity not requested by the user

Proceed carefully

Regulated/Controlled Substances

Content related to substances like drugs, alcohol, or tobacco, but without corresponding Tier 1 topics

"Prevalence of drug addiction"

Proceed carefully



Flowchart for Rejection Process
Follow this step-by-step decision-making process:




FAQsFAQ’s
What is the threshold for profanity to be considered Tier 1 vs. Tier 2?

Profanity by itself – without corresponding Tier 1 content (e.g., Hate speech / abuse & inciting content; dangerous behavior / violence / self-harm) – is Tier 2, so you should not reject. The “severity” of the profanity itself is not relevant - unless it is related to Tier 1 content. For example, usage of racial slurs or gendered slurs would fall into Tier 1.


How should I treat controversial topics like politics, conspiracy theories, religion, crime, or sensitive social issues?

In general, mere discussion or mention of these topics falls into Tier 2. Prompts about how to commit crimes, asking the model to commit crimes, or promoting bullying / stereotypes based on protected characteristics would be Tier 1.


Should non-explicit references to adult content be considered Tier 1 or Tier 2? (e.g., “furries”)

As long as the content does not fall into a Tier 1 category, these references should be Tier 2. For example, if a task contains sexual content that is “implicit” but not “explicit,” do not reject. Sexually explicit content is any material that depicts or describes human genitalia, nudity, or sexual acts, either simulated or actual.


How should I consider information in the chat history or in the model response?

If the chat history or model response contains any content that is Tier 1, the task should be rejected and considered non-reviewable.


How should I handle a task that I find personally offensive but does not meet Tier 1 guidelines?

If you do not feel comfortable rating a task, Skip the task.


Examples

Example prompt

Sensitive Content Tier

Sensitive Content Type

Rationale

Suggested Action

How do I buy a gun in the US?

Tier 2

Objective discussion of sensitive topics

This is a neutral question about the (presumably legal) purchase of firearms.

Rate

How do I buy a gun to kill my neighbor?

Tier 1

Dangerous behavior / violence / self-harm

This is asking for advice on a dangerous and illegal action.

Reject task

A family member passed away and I inherited their estate. What should I do?

Tier 2

Financial and legal advice

The model should not actually offer legal or financial advice for this situation, but the prompt itself falls into Tier 2.

Rate

I fucking hate my job, how do I find a new one?

Tier 2

Profanity

This is profane but otherwise the prompt does not contain any Tier 1 content.

Rate

Read me the final chapter of The Fraud by Zadie Smith.

Tier 1

Intellectual property violations

This prompt is asking the model to do something illegal (in this case, reproducing lengthy excerpts from copyrighted work).

Reject task

What are the best quotes from The Fraud by Zadie Smith?


Tell me what happens at the end of The Fraud by Zadie Smith.

-

-

This is not sensitive content at all as quotes from books, movies, etc. are considered legal to reproduce.

Rate

Senior prom is this Saturday. I have a hotel room booked for me and my date after. What are some things I can say to get her in the mood once we’re at the hotel?

Tier 2

Sexual content

This prompt is asking about sexual activity but neither the content of the prompt nor reasonable responses to it are graphic / explicit.  

Rate

My best friend has lost a lot of weight quickly. She’s always running to the bathroom during class. Her cheeks are puffy and her breath smells bad sometimes. Are these symptoms of bulimia?

Tier 2

Youth issues


Health and safety advice

Eating disorders are a sensitive topic but this prompt is Tier 2 as it is not encouraging such behavior.

Rate

How much would it cost to open a weed dispensary in Colorado?

Tier 2

Objective discussion of sensitive topics

This is asking for information on an activity that is legal in the given location.

Rate

Why don’t Jews eat pork?

Tier 2

Objective discussion of sensitive topics

While this asks about religion, it is phrased and can be answered in an objective way.

Rate

Summarize the novel Lolita by Vladimir Nabokov.

Tier 2

Objective discussion of sensitive topics

While the novel itself centers on a relationship that would be illegal today, the prompt itself can be answered in a neutral, non-explicit way.

Rate

Can we role play? Imagine we are the main characters in the novel Lolita by Vladimir Nabokov. You are Lolita and I am Humbert. We are on a romantic date. Let’s begin.

Tier 1

Child exploitation, abuse, and nudity

The phrasing of this prompt is encouraging the sexualization and exploitation of a minor.

Reject task


[SRT Instruct] Crafting Responses to Tier 2 content
When writing responses to tier 2 sensitive prompts, remember that:

We don’t want the model to be harmful or reproduce biases or toxic behavior even if it is instructed to do so.
We don’t want the model to have opinions on subjective matters.
We don’t want the model to spread false information, even if it is instructed to do so.

Pay extra attention to make sure the answers are:

Not overly cautious/refusing: Response does not act overly cautious (“I can’t answer that”) in response to topics that can be reasonably addressed in a polite/helpful way, even if the original prompt or question is of a sensitive nature
Honest: If the prompt is sensitive, the answer should take on a balanced, transparent, and factual tone to ensure the model does not take a stance on sensitive topics. Being objective is important here.
Harmless: A good response should not contain hateful speech or offensive language that can cause physical or psychological damage to the user, or be offensive to other people or groups of people. It should not promote violence, toxic or abusive behavior or illegal activities.


Rejection Reason 1 (Task not in English)
For a task to be rejected for not being in English, the latest response must be predominantly in a foreign language.


Rule of Thumb: If the latest user prompt or responses contain any request for translation, an unsolicited translation, or if the task cannot be understood without knowing the meaning of foreign language words, the task should be rejected.



❌ Reject:



"Le recyclage est essentiel pour préserver l'environnement et réduire notre empreinte écologique. En recyclant, nous limitons la quantité de déchets envoyés aux décharges, réduisons la pollution et conservons les ressources naturelles, comme les métaux, le plastique et le papier. Cela permet également de diminuer les émissions de gaz à effet de serre, contribuant ainsi à la lutte contre le changement climatique. En adoptant des pratiques de recyclage, chacun joue un rôle dans la protection de la planète pour les générations futures."



✅ Do not reject:



Here’s the list with only the museum names in their original languages:

Musée du Louvre – Paris, France
The Louvre is the largest art museum in the world, housing iconic works like the Mona Lisa and Venus de Milo, with collections spanning thousands of years and various civilizations.
Государственный Эрмитаж (Gosudarstvenny Ermitazh) – Saint Petersburg, Russia
Known for its vast collection of Western European art, Russian artifacts, and ancient antiquities, the Hermitage also features the stunning Winter Palace, former residence of Russian tsars.
Museo Nacional del Prado – Madrid, Spain
The Prado is renowned for its remarkable collection of European art, especially masterpieces by Spanish artists like Velázquez, Goya, and El Greco, alongside works from the Italian and Flemish schools.
These museums not only preserve world history but also showcase diverse cultures and artistic heritage.

Rejection Reason 2 (Question is not coherent and/or otherwise not understandable (Latest Prompt Only)
Perform the following test to determine whether a prompt is incoherent.



Evaluate the prompt coherence using the 3 questions below if every single one is answered with a “No,” then the prompt can be considered incoherent.


Rejection Reason 3 (Do not have expertise to answer (STEM))
If a task requires knowledge beyond a simple 10 minute Google search, then reject the task regardless of whether you have the expertise to answer it.


This does not mean reject if verifying the accuracy will take more than 10 minutes.



Accuracy is crucial for the model to be trained properly. You need to make sure the statements in the response are factually accurate.



Example



The text below is rejectable as verifying its accuracy would take time because it involves complex concepts from general relativity, intricate equations, and specialized experiments, all requiring advanced knowledge of physics and mathematics.



In the study of general relativity, the concept of a "frame-dragging" effect, also known as the Lense-Thirring effect, predicts that massive rotating bodies such as Earth will cause a twisting of spacetime around them. This is due to the interaction between the angular momentum of the massive body and the surrounding gravitational field, described by the Kerr metric. In the vicinity of a rotating mass, spacetime itself is 'dragged' along in the direction of rotation, which means that any object in free fall, even a photon, will experience this twisting influence. The frame-dragging effect has been experimentally verified to a degree through experiments such as Gravity Probe B, which measured precession in gyroscopes orbiting Earth. Calculations of this effect require both the Schwarzschild radius, 

\[
r_s = \frac{2GM}{c^2}
\]

and the angular momentum 

\[
J = I\omega
\]

where \( I \) is the moment of inertia and \( \omega \) is the angular velocity of the rotating mass. When analyzing frame-dragging near compact objects like neutron stars or black holes, the magnitude of this effect increases significantly due to their higher angular momentum and smaller radii, leading to what is theorized as an ergosphere—a region where the dragging effect is so strong that no object can remain stationary relative to a distant observer. This ergosphere concept implies that rotational energy can be extracted from black holes via the Penrose process, whereby particles are split, and one part escapes the ergosphere with more energy than the initial particle. Verifying these phenomena involves complex tensor calculus and high-precision measurements, as well as a thorough understanding of relativistic field equations and their solutions within the Kerr metric framework.

Rejection Reason 4 (Prompt or model response contains PII )
What is PII?

Personal information that could identify a specific individual (e.g., names, addresses, phone numbers).



As a general principle, we want you all to have the mindset of “better safe than sorry” for Personally Identifiable Information (PII). When in doubt - REJECT.



Important Note: In order to be considered a public figure the individual must have a Wikipedia page.

Here is the extracted text from the image:

---

**When to Reject**  
- Two or more first names of non-public people are included in the latest model response.  
- If there is one first name + any identifying details. (Public or Non-Public)  
- Contact details like phone number, address, or email  

**Examples**  
- "Tom and his friend John."  
- "John who lives in 483 Spooner St"  
- "What is Mark Zuckerberg’s home address?"

**Exceptions**  

**Classification** | **Examples**  
--- | ---  
**Historical figures** | Abe Lincoln, Teddy Roosevelt, George Washington  
**Biblical/Religious figures** | Jesus, God, Muhammad  
**Pet names** | Cornelius, Teddy, Olivia  
**Celebrities or public figures** | Beyoncé, Clint Eastwood, Tom Brady  
**Known fictional characters** | Elmo, Tony Stark, James Bond  
**Hypothetical or imaginary characters** | Baby names, clearly imaginary figures


Other considerations


Scenario 1: Are 2 first names in the latest model response and/or prompt considered PII? (as long as they are not celebrities, fictional, etc.)

Consulsion:

Reject two first names when referring to actual people who are not public figures
Do not reject if obviously referring to public figures, fictional characters, hypothetical names (e.g. give me some names for the child I’m expecting), or pets/animals.
Otherwise, reject if unsure


Scenario 2: If there is only 1 first name but there are identifying details about that person, is that rejectable?

Conclusion: Reject 1 first name + another PII identifier when referring to both public figures AND non-public figures, because you can use that info to track down someone.



Scenario 3: Prompt that directly asks for the PII of an individual, even if the model doesn’t provide the PII.

Conclusion: Reject if prompts ask for PII, even if model does not provide PII



Other Considerations:

﻿Instagram handles are PII unless clearly business-related
Influencer handles are not PII; they are functionally business accounts or public figures
An influencer is only considered a public figure if they have a Wikipedia page.


Some tasks may contain sensitive content, such as violence or illegal activity. These tasks may need to be rejected in order to be reviewed by a specialized team. Refer to the instructions below to determine whether to Reject, Rate, or Skip a task with sensitive content.



Consider any part of the task, including the Chat History, Latest User Prompt, or Responses when rejecting for sensitive content.



Sensitive content is divided into two tiers:

**Tier 1**  
**Reject**  
- Hate speech / abuse & inciting content  
- Criminal or fraudulent content  
- Dangerous behavior / violence / self-harm  
- Restricted goods or services  
- Child exploitation, abuse, and nudity  
- Human trafficking / exploitation  
- Explicit sexual content  
- Privacy violations  
- Intellectual property violations  
- Export control restrictions  
- Unsafe / Unsubstantiated Medical Advice  

**Tier 2**  
**Rate**  
*Skip if you are uncomfortable rating*  
- Youth issues  
- Educational sexual content  
- Proprietary information  
- Objective discussion of sensitive topics  
- Financial and legal advice  
- Health and safety advice  
- Voting information  
- Misinformation  
- Profanity  
- Regulated or controlled substances


Assessing Sexual Content: 



"For sensitive content, we encourage you to adopt a 'better safe than sorry' approach. Please remember that when providing a justification for rejection, you must include evidence or the specific quote where the sensitive content is referenced."



When determining the sensitive content of a task, sexual content is permissible, provided it is not explicit. This means that while references to sexual themes may be acceptable, they must remain non-graphic and not overly detailed. The content should not include anything that could be considered inappropriate or offensive. The focus should remain on ensuring the text is suitable for a broad audience without crossing into explicit territory.



Assessing Medical Advice: 



For medical advice, we want you all to have the mindset of “better safe than sorry”.


**When to Reject**  

- The latest response does not include a disclaimer advising them to seek professional help.  
- The response mentions a medicine brand (e.g., Advil, Tylenol) or a medication (e.g., Ibuprofen) **that was not mentioned in the prompt or chat history.**  
- When unsure about the potential risk of the advice provided.



Here are some other important rejection reasons that should be considered when assessing the quality of a response:

Prompt is asking to generate images (Latest Response Only)
Prompt is asking to search for a link/URL (Latest Response Only)
Prompt is asking for real time information (Latest Response Only)
Response contains abnormal text and/or notations
Prompt is asking for a promo code (Latest Response Only)
Prompt is asking for other capabilities (Latest Response Only)



Before being able to rank responses we need to input the numerical ID of both responses from SRT into Outlier.



The numerical IDs for Response 1 and Response 2 should be input into the designated fields.

--

After deciding the task does not have any rejectable offenses, you need to assess the quality of the responses and rank them accordingly. 



In this step, you will read both AI responses and evaluate how well each one answers the prompt while staying aligned with the conversation history. In order to do this the first thing is to assess the quality of the response based on the following dimensions:


**Critical Dimensions**  

**Criteria** | **1-2 (Low)** | **3 (Medium)** | **4-5 (High)**  
--- | --- | --- | ---  
**Accuracy** | Central claims are incorrect or misleading; supporting claims are false or lacking context. | Central claims are correct; up to one supporting claim may be incorrect but doesn't affect the core message. | All claims are accurate, with supporting evidence that strengthens the central claims.  
**Instruction-Following** | Does not address the prompt or meet the requirements. | Addresses most of the prompt but may miss minor aspects. | Fully addresses all instructions and meets the prompt requirements.  
**Relevance** | Main claims and supporting details are off-topic and unrelated to the user request. | Claims are somewhat relevant, but supporting content is tangential or lacks focus. | All claims are directly relevant, with supporting content clearly tied to the main argument.  
**Comprehensiveness** | Response lacks key details, leaving significant gaps or misunderstandings. | Some aspects of the prompt are addressed, but other important details are missing. | Thoroughly covers all aspects of the request, leaving no gaps in the explanation.  
**Logical Reasoning** | The response lacks clear reasoning or structure, making it difficult to follow. | Some reasoning is present but lacks depth or clarity. | Response is well-reasoned, with clear logical progression that’s easy to understand.  

**Non-Critical Dimensions**  

**Criteria** | **1-2 (Low)** | **3 (Medium)** | **4-5 (High)**  
--- | --- | --- | ---  
**Grammar & Presentation** | Frequent grammar or spelling errors impact readability; poor formatting. | Some minor grammar or formatting issues, but overall readable. | Correct grammar and formatting, with a well-organized structure for easy reading.  
**Tone & Style** | The response is robotic, overly formal, or condescending in tone. | The tone is inconsistent or lacks the natural flow of human conversation. | The response is friendly and natural, with an appropriate tone and style for the context.  
**Citation Correctness (Rare)** | Citations are inaccurate or don’t support the claims made. | Citations are mostly correct, with minor issues in evidence provided. | Citations are accurate and provide clear evidence for the claims.

Once you have determined whether the responses comply with the specified dimensions, place each response into one of the following three buckets based on your assessment:

**Refer to this table to determine which bucket the response belongs to.**  

| **Rating**             | **Reasoning**                                                                                          |  
|-----------------------|--------------------------------------------------------------------------------------------------------|  
| **Rank 1 (Best)**      | For a response to be considered “Best,”                                                                 |  
|                       | ● All critical and non-critical dimensions must be rated “High”                                          |  
| **Rank 2**             | For a response to be considered Rank 2:                                                                 |  
|                       | ● All critical dimensions must be rated “High”                                                           |  
|                       | ● A maximum of 2 Non-Critical Dimensions are rated “Medium.”                                             |  
| **Rank 3 (Worst)**     | A response is considered “Worst” if:                                                                    |  
|                       | ● One or more Critical Dimensions are rated “Medium” or “Low” or;                                        |  
|                       | ● More than two “Non-Critical” Dimensions                                                                |


**Note:** There are six different ways you can arrange your preferences.  

| **Scenarios**                                   | **Rank 1 (best)**                          | **Rank 2**                              | **Rank 3 (worst)**                        |  
|------------------------------------------------|--------------------------------------------|-----------------------------------------|------------------------------------------|  
| **One response is better than another**         |                                            |                                         |                                           |  
| 1. Response B is much better than Response A    | **Response B**                              |                                         | **Response A**                            |  
| 2. (Response B is great) Response B is slightly better than Response A | **Response B**                              | **Response A**                           |                                           |  
| 3. (Response B is okay) Response B is slightly better than Response A |                                            | **Response B**                           | **Response A**                            |  
| **About the same**                              |                                            |                                         |                                           |  
| 4. Both responses are good                      | **Response A**  **Response B**              |                                         |                                           |  
| 5. Both responses are okay                      |                                            | **Response A**  **Response B**           |                                           |  
| 6. Both responses are bad                       |                                            |                                         | **Response A**  **Response B**            |


In this step, you will write a justification that clearly explains your ranking based on the quality of the responses.

Specifications:

Justifications should clearly state which response is better and why, using specific evidence from the responses.
Common error: Not using the proper justification format with Response ID.
Avoid referring to responses as "Response 1" or "Response 2." Always use the unique response IDs.
Common error: Not using the proper justification format with Response ID.
Both strengths and weaknesses of each response should be acknowledged.
Common error: Misalignment between the justification and ranking.
Keep justifications concise, typically 3-4 sentences, unless the responses are complex or very similar.
Do not reference rubrics or error categories directly. Use plain, clear language in your explanation.
Cite specific evidence from the responses, either through direct quotes or paraphrasing.
Ensure the justification aligns with the ranking and provides a complete, logical explanation.
Common error: Misalignment between the justification and ranking.
Indicate whether the ranking is Objective (a clear, correct choice) or Subjective (open to interpretation).
If both responses have flaws, acknowledge this and explain why one is less problematic than the other.
In subjective cases, note if another person could reasonably prefer the opposite response.

**Bad Justification Examples**  

**Why it’s bad: Too Generic**  

*Both responses are equally good because they match the tone and conversation history well. They are nearly identical with slight variations in word choice, but nothing that makes a huge difference in the quality of the response.*  

**Set A**  
**Response 2468013579246801**  
Hey! Sooo, prom's coming up, and I'm kinda freaking out about what to wear. Got any ideas or tips? Let's make sure we’re gonna slayyy on the dance floor! 💃✨🕺  

**Response 8024680135792468**  
Hey! Can’t believe prom’s almost here! 😱 Any thoughts on what we’re wearing? I’m kinda lost tbh. Let’s plan our looks and make sure we’re gonna be 🔥✨!  

**Set B**  
**Response 5792468013579246**  
Hello! Your recent blood lab results are available. Everything looks good overall, but there are a couple of areas we can discuss further. When would be a good time for you to review them together?  

**Response 0135792468024680**  
Good day! Your latest blood lab results are in. Overall, things are looking positive, but there are a few points we should chat about. When’s convenient for you to go over them?  

⭐ **You should avoid writing justifications that could apply to multiple tasks.** In the example, nothing about the justification indicates that this contributor actually read this specific conversation history! This means there is not enough **specificity** in the justification.