You have been tasked with constructing a Learning Station on the basic
operating system commands for the Linux platform. The shape of your
Learning Stations solves a challenging problem on Bandit at OverTheWire
(OTW).

## Your learning station must include at the minimum: 

-   Evidence you solved up to bandit10 for year 11 students and 15 for
    year 12 students who\'ve done the previous 10 before. Note: if you
    have done more than 15 last year, do five more than where you were
    at.

-   Material for learning stations that covers more than one of the
    following commands (you\'ll likely need to do an exercise from
    bandit 6+):

    -   file

    -   find

    -   du

    -   grep

    -   sort

    -   uniq

    -   strings

    -   base64

-   Note, you are not writing man articles on the commands. Instead, you
    are teaching someone how to solve a bandit problem that may require
    multiple commands.

## Learning Stations

What is a learning station? In education, Learning Stations are points
of interest in a classroom that provides learners with the opportunity
to step through a problem, teaching them to identify the different steps
and highlighting how to solve them.

Our version of Learning Stations will consist of [markdown
documents](https://www.markdownguide.org/cheat-sheet/) and potentially
additional elements needed to teach, inform, or explain the scenario.
Markdown Documents are similar to web pages but come with a lightweight
formatting guide. Check the cheat sheet above or the style guide below
for more information.

Use the template markdown provided with this assignment to help frame
your work. Also, look at the cookbook articles on our GitHub for
examples of how things have been broken down.

Remember, the goal of the process is not to show them the commands they
need to solve the problem but to inform or educate them on how they
could replicate, why they might care, etc.

In essence, you must provide a

-   Introduction to the problem being solved

-   An explanation of the solution

-   An explanation of the different commands and how they work

-   (extension) An analysis/evaluation/comparison of different commands
    may also solve the problem.

-   Feel free to add other material that you feel is essential to your
    learning station

### Learning Stations vs Cookbooks Recipes

In my classes, I create many Recipes for students to follow. Learning
Stations are similar to recipes. However, a recipe is intended to be
supported by lectures/direct teacher support. They can also focus on
people with deep technical literacy learning a new skill.

An example of a technical recipe can be seen here:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="configuring-the-router-via-tftp">Configuring the router via TFTP</h2>
<h3 id="problem">Problem:</h3>
<p>You want to load configuration commands via TFTP.</p>
<h3 id="solution">Solution:</h3>
<p>You can use the copy TFTP: command to configure the router via the Trivial File Transfer Protocol (TFTP)</p>
<p><img src="C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image5.png" style="width:5.83333in;height:2.275in" alt="Text Description automatically generated" /></p>
<h3 id="discussion">Discussion:</h3>
<p>Generally, most people configure their routers using telnet/ssh and the configured terminal command. However, people tend to resort to cutting and pasting a large set of commands for significant configuration changes. While this method works, it is inefficient and slow, particularly if you have to configure many routers. </p>
<p>Using TFTP to download a large set of configuration commands, the router doesn't need to echo each character to your screen, reducing the overhead and increasing the interaction speed. </p>
<p>In this example, the router is configured by downloading a file called NEWCONFIG from a server at 192.168.10.1 using the Trivial File Transfer Protocol (TFTP). The router will copy the entire file by TFTP before entering the commands into the running configuration. </p>
<p>Using TFTP is helpful because sometimes, some commands in the middle of a configuration could disrupt your access to the router, but the rest of the commands might fix the problem. If you tried to enter them manually using telnet/ssh and configure the terminal, you could lock yourself out of the router. A typical example of this problem happens when you replace an active access list. When you enter the first line, the router puts an implicit deny-all at the end, which can break your session. Using TFTP avoids this problem.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You can see how the author of this recipe broke their response into
multiple chunks.

### Explanation:

![](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image6.png){width="4.382268153980752in"
height="3.0597222222222222in"}

*Explanation of the problem and the solution*

In the example above, the author explains the problem and the solution.
In both cases, it is very superficial and intended to draw a reader\'s
attention to a specific problem.

### Analysis: 

![](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image7.png){width="4.3737007874015745in"
height="1.212386264216973in"}

*An analysis of the problem and solution*

Next, the author details the underlying problem (copy and pasting) that
needs to be addressed. This form of analysis highlights to the reader
why they should consider the alternative presented in this recipe.

### Evaluation:

![Text Description automatically
generated](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image8.png){width="4.154162292213473in"
height="1.488888888888889in"}

*Explanation and evaluation*

Finally, the author goes through and explains the solution and then
evaluates the default solution against the new solution.

## The difference between recipes and learning stations

Notice how the recipe above has many assumptions? We assume that the
reader knows that TFTP exists, that they understand terminology like
active access lists, what deny-all is, or even what sessions are. These
elements were controlled (more or less) by being in a structured
classroom environment: lectures, worksheets, prior experience, and
scaffolded learning supplement recipes.

Learning Stations, however, make fewer assumptions. They assume that the
reader knows very little about what they are doing or why they need to
do it. In your case, you will need to spend more time explaining what
different commands are, why the reader cares about them, and potentially
identify how the reader can identify that problem in the future.

# OverTheWire

OverTheWire (OTW) is a CTF lite training tool to help people new to
Linux Administration to learn essential and valuable tools.

<https://overthewire.org/wargames/bandit/bandit0.html>

Each level sets the goals required for completing the level including
some valuable commands.

![Text Description automatically
generated](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image9.png){width="6.268055555555556in"
height="3.9791666666666665in"}

You will see that they suggest commands you may need to solve this
level. In this case, it is ssh. How can we use this?

Open terminator, and in the prompt, type man ssh

If you can\'t use man for some reason, you could search for it on
google:

<https://linux.die.net/man/1/ssh>

Learning how to read man files is an important skill. However, don\'t be
afraid to supplement your knowledge by abusing google.

## Submission Guide

### Evidence of Bandit 1 -- 10 \| 1 - ?+5

At the minimum:

-   A visual representation of all of the levels you\'ve solved.

### Learning Station

-   Introduction to the problem being solved

-   An explanation of the solution

-   An explanation of the different commands and how they work

-   (extension) An analysis/evaluation/comparison of different commands
    may also solve the problem.

-   (extension) other material that you feel is essential to your
    learning station

## Rubric

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 39%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Knowledge, Comprehension &amp; Application</strong></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CRITERIA</strong></td>
<td><strong>EXPECTATIONS</strong></td>
<td><strong>POSS</strong></td>
<td><strong>STUDENT</strong></td>
<td><strong>GIVEN</strong></td>
<td><strong>MULTI</strong></td>
<td><strong>TOTAL</strong></td>
</tr>
<tr class="even">
<td><strong>Bandit Levels</strong></td>
<td><p>You have provided <strong>appropriate evidence of completing Bandit levels</strong> on OverTheWire.</p>
<p>Students doing Networking for the first time:</p>
<ul>
<li><p>Bandit 0</p></li>
<li><p>Bandit 1 – 5</p></li>
<li><p>Bandit 6 – 10</p></li>
</ul>
<p>Students doing Networking for the second time:</p>
<ul>
<li><p>Bandit 0 – 5</p></li>
<li><p>Bandit 6 – 10</p></li>
<li><p>Bandit 11 – 15 (or +5 from last time)</p></li>
</ul>
<p>Evidence for knowledge, comprehension, and application may include:</p>
<ul>
<li><p><strong>Knowledge</strong>: Your evidence highlights that you recall and list relevant terms in your learning. It may tell a story to the reader (the teacher) or state the conditions of your learning.</p></li>
<li><p><strong>Comprehension</strong>: Your evidence highlights that you can identify critical aspects of your learning or explain what you've done to the author.</p></li>
<li><p><strong>Application</strong>: It is clear from your evidence that you constructed a complete submission</p></li>
</ul></td>
<td><p>2</p>
<p>2</p>
<p>2</p></td>
<td><p>__/2</p>
<p>__/2</p>
<p>__/2</p></td>
<td><p>__/2</p>
<p>__/2</p>
<p>__/2</p></td>
<td>-</td>
<td>__ / 6</td>
</tr>
<tr class="odd">
<td><p><strong>Learning Station</strong></p>
<p>(individual)</p></td>
<td><p>You have <strong>submitted one learning station</strong> in <strong>markdown format</strong>. Your learning stations <strong>appear to adequately explain how to solve the problems</strong> using available tools and techniques.</p>
<p>Evidence for knowledge, comprehension, and application may include:</p>
<ul>
<li><p><strong>Knowledge</strong>: Your evidence highlights that you recall and list relevant terms in your learning. It may tell a story to the reader (the teacher) or state the conditions of your learning.</p></li>
<li><p><strong>Comprehension</strong>: Your evidence highlights that you can identify critical aspects of your learning or explain what you've done to the author.</p></li>
<li><p><strong>Application</strong>: It is clear from your evidence that you constructed a complete submission</p></li>
</ul>
<p>e</p>
<p>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</p></td>
<td>2</td>
<td>__/2</td>
<td>__/2</td>
<td><p>A x2</p>
<p>T x1</p></td>
<td>A __/ 4<br />
T __/ 2</td>
</tr>
<tr class="even">
<td><strong>OS commands</strong></td>
<td><p>You have submitted evidence that you address multiple Linux commands common in bandit6-10 in the problems you have solved.</p>
<p>Evidence for knowledge, comprehension, and application may include:</p>
<ul>
<li><p><strong>Knowledge</strong>: Your evidence highlights that you recall and list relevant terms in your learning. It may tell a story to the reader (the teacher) or state the conditions of your learning.</p></li>
<li><p><strong>Comprehension</strong>: Your evidence highlights that you can identify critical aspects of your learning or explain what you've done to the author.</p></li>
</ul>
<p><strong>Application</strong>: It is clear from your evidence that you constructed a complete submission</p></td>
<td>2</td>
<td>__/ 2</td>
<td>__/ 2</td>
<td><p>A x2</p>
<p>T x1</p></td>
<td><p>__/4</p>
<p>__/2</p></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Analysis, Synthesis &amp; Evaluation</strong></td>
<td colspan="2"></td>
<td colspan="2"><strong>SUB TOTAL</strong></td>
<td><p><strong>A _ / 14</strong></p>
<p><strong>T _ / 10</strong></p></td>
</tr>
<tr class="even">
<td><strong>Learning Station Communication</strong></td>
<td><p>You have submitted <strong>evidence of your learning station</strong> on a Bandit problem on OverTheWire.</p>
<p>Your evidence highlights <strong>how you express yourself</strong> using appropriate evidence and accurate sources. It also considers <strong>your ability to communicate accurately</strong> with others using <strong>correct terms</strong> in appropriate formats.</p>
<p>Evidence for higher-order learning may include:</p>
<ul>
<li><p><strong>Analysis</strong>: Your evidence shows a reasoned understanding of what you did and why. For example, you may have explained how you did X, Y, and Z, but you continue to explain why you did them the way you did.</p></li>
<li><p><strong>Evaluative</strong>: your evidence makes a judgement of something or between multiple things. This judgement may be the value of one thing over another or highlighting the significant differences between two things.</p></li>
<li><p><strong>Transferal</strong>: your evidence highlights when you apply information, strategies, or skills that you have learnt to a new situation or context.</p></li>
</ul>
<p>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</p></td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td>-</td>
<td>__/ 4</td>
</tr>
<tr class="odd">
<td><strong>Learning Station Technical Understanding</strong></td>
<td><p>You have submitted <strong>evidence of learning station on a Bandit problem</strong> on OverTheWire.</p>
<p>Your evidnece highlights <strong>your understanding</strong> of <strong>common commands</strong> for operational commands on Linux systems and <strong>implications of security considerations.</strong></p>
<p>Evidence for higher-order learning may include:</p>
<ul>
<li><p><strong>Analysis</strong>: Your evidence shows a reasoned understanding of what you did and why. For example, you may have explained how you did X, Y, and Z, but you continue to explain why you did them the way you did.</p></li>
<li><p><strong>Evaluative</strong>: your evidence makes a judgement of something or between multiple things. This judgement may be the value of one thing over another or highlighting the significant differences between two things.</p></li>
<li><p><strong>Transferal</strong>: your evidence highlights when you apply information, strategies, or skills that you have learnt to a new situation or context.</p></li>
</ul>
<p>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</p></td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td><p>A x1</p>
<p>T x2</p></td>
<td><p>A __/ 4</p>
<p>T __/ 8</p></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Submission Guidelines</strong></td>
<td colspan="2"></td>
<td colspan="2"><strong>SUB TOTAL</strong></td>
<td><p><strong>A __/ 8</strong></p>
<p><strong>T__/12</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Quality of Submission</strong></td>
<td><strong>Assessment submission is ordered</strong> and has a definite pattern to its construction. <strong>The reader is not confused about the content in any given section and can follow the submission flow</strong> easily. </td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td>X1</td>
<td>__ / 4</td>
</tr>
<tr class="even">
<td><strong>Formatting</strong></td>
<td><strong>Students have</strong> <strong>followed the formatting instructions,</strong> including any provided templates and guides <strong>or have created their own</strong> legible formatting guide <strong>and applied it constantly</strong>.</td>
<td>2</td>
<td>__/2</td>
<td>__/2</td>
<td>-</td>
<td>__ / 2</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"><strong>SUB TOTAL</strong></td>
<td><strong>__ /6</strong></td>
</tr>
<tr class="even">
<td></td>
<td>DAYS LATE ___/7 = ___%</td>
<td></td>
<td></td>
<td colspan="2"><strong>FINAL</strong></td>
<td><strong>A __/28<br />
T __/28</strong></td>
</tr>
</tbody>
</table>

## Rubric sections

##### Section 1: Knowledge Comprehension and Application

This section of the rubric consists of the required elements of the
assignment. Students should take special care to include ALL these
elements as they are often extended in the following sections

##### Section 2: Analysis, Synthesis, and Evaluation. 

This section will evaluate your ability to include critical thinking and
justification elements into your work. Often the requirements for
extension are not explicitly given, so it will be up to you to decide
how best to demonstrate what you have learned beyond the required unit
goals and curriculum. Items such as 3D models, pictures, drawings,
diagrammatic responses, notes, evidence of problem-solving, advanced
programming concepts, elegant responses, media, etc., are all available
options.

##### Section 3: Submission Guidelines 

Students are expected to provide a submission that fulfils the
requirements listed in style guides while also submitting at an
appropriate quality. Be aware that points in this section could be 2- or
4-point items. Treat them accordingly.

## Submission

All submission items should be stored in an appropriate format. For
example, code must be stored in a programmatical format so it can be
evaluated (**images of code or code copied and pasted into a document
may not be marked**)

Evidence of working material must be recorded where appropriate. For
example, to show how your robot meets a requirement, you must submit a
recording of it completing that requirement. Similarly, if you need to
show how your program can download a file from the internet and crack a
password, you must submit a recording of it doing that.

Ask the teacher if you are unsure if an element needs to be
recorded**.**

All materials must be submitted to Google Classroom.

Students are responsible for keeping backups/master copies.

**\
**

## **Scoring Notes**

Formatting for all typed/written assessments should be as follows:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Google Doc</strong></th>
<th><em>11-12 Pt</em></th>
<th><em>1.15-1.5 Line Spacing</em></th>
<th><em>1 Space between paragraphs</em></th>
<th><em>Spelling and Grammar “Soft Limit”</em></th>
<th><em>In-Text Citations with footnotes</em></th>
<th rowspan="2"><p><em>Title Page/Slide:</em></p>
<ul>
<li><p><em>Name</em></p></li>
<li><p><em>Date</em></p></li>
<li><p><em>Class</em></p></li>
<li><p><em>Aim</em></p></li>
<li><p><em>Assessment title</em></p></li>
</ul></th>
</tr>
<tr class="odd">
<th><strong>Slides</strong></th>
<th><p><em>10-12 pt. font text</em></p>
<p><em>14-24 pt. font titles</em></p></th>
<th><em>1.0 1.15 Line Spacing</em></th>
<th><em>Bullet Points Preferred</em></th>
<th><em>Word Count per slide &gt;100-110 “Soft Limit.”</em></th>
<th><em>Approved Templates and Themes</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Python</strong></td>
<td colspan="6"><p><em>We apply the following style guide to Python files. However, in general, most programs follow this overall layout.</em></p>
<p><img src="C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image1.png" style="width:5.29167in;height:4.11736in" /></p>
<p><a href="https://pep8.org/">PEP 8: The Style Guide for Python Code</a></p></td>
</tr>
<tr class="even">
<td><p><strong>Arduino</strong></p>
<p><strong>C/C++</strong></p></td>
<td colspan="6"><p><em>We apply the following style guide to C/C++ files. However, in general most programs follow this broad layout.</em></p>
<p><img src="C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image2.png" style="width:5.10488in;height:3.13585in" /></p>
<p><em>I accept both K&amp;R and K&amp;R alternative bracing format. As long as it is consistent in your file.</em></p>
<p><a href="https://docs.arduino.cc/learn/contributions/arduino-library-style-guide">Arduino Style Guide for Creating Libraries | Arduino Documentation | Arduino Documentation</a></p></td>
</tr>
<tr class="odd">
<td><strong>Markdown</strong></td>
<td colspan="6"><p><em>We apply the following style guide to markdown documents. However, in general, most documents follow some variation of the following layout:</em></p>
<p><img src="C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image3.png" style="width:5.29167in;height:3.41851in" /></p>
<p><a href="https://github.com/google/styleguide/blob/gh-pages/docguide/style.md">https://github.com/google/styleguide/blob/gh-pages/docguide/style.md</a></p></td>
</tr>
</tbody>
</table>

"Soft Limits" are not rigidly defined limits and will be assessed on a
case-by-case basis. Ask for clarification on specific tasks

## Possible Scoring Groups are out of 2 or 4 Points. 

##### 2-Point Criteria - Knowledge and Understanding

Criteria assessed as 2-Points are classified as Knowledge and
Understanding criteria. These will examine and evaluate a student's
ability to effectively state facts and define terms and concepts.
Analysis and synthesis of the information will not be assessed through
these criteria.

|                        | ***0 Points***                                                            | ***1 Point***                                                                          | ***2 Points***                                                                    |
|------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| ***2 Point Criteria*** | ***Not present** or **not able to be assessed** as the required criteria* | *Item is presented but **does not meet expectations** for quality, rigour, or detail.* | *Item is presented and **does meet expectations** for quality, rigour, or detail* |

##### 4-Point Criteria - Analysis and Synthesis and Expert Review

To show true mastery of your developing skills, students must show that
they can go beyond simple repetition of the given tasks or an
explanation of processes. Students will demonstrate their ability to
show higher-order thinking through analysis, evaluation, or linking
multiple fields of learning to solve problems in novel ways.

## Analysis and Synthesis

Analysis and Synthesis components evaluate a student's ability to
effectively review data and understandings and develop these into a
coherent and relevant statement. Analysis refers to the generating of
thoughts from interpreting the data. In contrast, synthesis combines
experience from one area with other pertinent knowledge to develop an
original and compelling solution.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><em><strong>0 Points</strong></em></th>
<th><em><strong>1 Point</strong></em></th>
<th><em><strong>2 Points </strong></em></th>
<th><em><strong>3 Points</strong></em></th>
<th><em><strong>4 Points</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>4 Point Criteria</strong></em></td>
<td><em><strong>Not present</strong> or <strong>not able to be assessed</strong> as the required criteria</em></td>
<td><em>Evidence is presented and explained. However, it <strong>does not show appropriate evidence of higher-order thinking</strong> such as analysis, evaluation, or synthesis.</em></td>
<td><em>Evidence is presented and <strong>shows appropriate evidence of higher-order thinking</strong> such as analysis, evaluation, or synthesis.</em></td>
<td><p><em>Evidence is presented and <strong>exceeds expectations for evidence of higher-order thinking</strong> such as analysis, evaluation, or synthesis.</em></p>
<p><em><strong>-or-</strong></em></p>
<p><em>Item is presented and shows appropriate evidence of higher-order thinking such as analysis, evaluation, or synthesis and <strong>exceeds expectations for quality or rigour</strong> of understanding of the selected mastery.</em></p></td>
<td><em>Evidence is presented and <strong>exceeds expectations for evidence of higher-order thinking</strong> such as analysis, evaluation, or synthesis. <strong>Additionally, this item exceeds expectations for quality or rigour</strong> of understanding of the selected mastery.</em></td>
</tr>
</tbody>
</table>

##### Expert Review

Expert Reviews evaluate a student's ability to build solutions using the
skills taught during the semester. Criteria assessed as 4-Points are
classified as Analysis and Synthesis criteria. These will examine and
evaluate a student's ability to effectively review data and
understandings and develop these into a coherent and relevant statement.
Analysis refers to the generating of thoughts from interpreting the
data. In contrast, synthesis combines experience from one area with
other pertinent knowledge to develop an original and compelling
solution.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><em><strong>0 Points</strong></em></th>
<th><em><strong>1 Point</strong></em></th>
<th><em><strong>2 Points </strong></em></th>
<th><em><strong>3 Points</strong></em></th>
<th><em><strong>4 Points</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>4 Point Criteria</strong></em></td>
<td><em><strong>Not present</strong> or <strong>not able to be assessed</strong> as the required criteria</em></td>
<td><em>Evidence is presented and broadly solves the problem. However<strong>, the evidence does not show appropriate mastery</strong> upon review.</em></td>
<td><em>Evidence is presented and broadly solves the problem. On review, it <strong>does show appropriate evidence</strong> of mastery.</em></td>
<td><p><em>Evidence is presented and solves the specific problem. On review, the evidence <strong>shows understanding beyond expected mastery</strong>.</em></p>
<p><em><strong>-or-</strong></em></p>
<p><em>Item is presented and broadly solves the problem. On review, it does show appropriate evidence of mastery and is <strong>done so in a well-constructed or design method</strong> that clearly shows higher levels of understanding<strong>.</strong></em></p></td>
<td><em>Evidence is presented and solves the specific problem. On review, <strong>the evidence shows understanding well beyond expected mastery</strong> and is <strong>done so in a well-constructed or designed method</strong> that clearly indicates higher levels of understanding.</em></td>
</tr>
</tbody>
</table>

##### Multiplier

Criteria will be combined with a **Multiplier**. While each criterion
will be scored on the 0-1-2-4 scale, the multiplier will attach relevant
worth to each criterion. Be aware of these multipliers and dedicate
appropriate time to ensure you achieve your best result.

## Achievement Standards: 

## Evidence of higher-order learning: 

What is it that I mean by "higher-order thinking"?

It means I want you to go beyond replicating what we do in class. I want
you to dig into your brain and understand why you did something, what
about it was great, and what could be improved.

Why is this important? Reflective thinkers can go beyond what they are
taught and can customise their learning to ben

![](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image4.png)

##  
