**Task**

You are tasked with the creation of a Cookbook and the completion of
networking challenges.

**Each submission must include the following at a minimum**

-   A cookbook containing three recipes.

-   Each recipe follows the following process:

    -   Problem being solved

    -   How does solving this problem help?

    -   Explanation of procedure to solve the problem

    -   Analysis \| Evaluation \| Compare \| Contrast \| "Story."

-   Challenge Response.

# Tools of Learning

### Cookbook

A cookbook is a collection of recipes that are often themed. In
Information Technology, cookbooks are prolific and are themed around
current problems that you might face in some domain.

<https://www.librarything.com/nseries/7655/OReilly-Cookbook-series>

### Recipes (technical)

Technical recipes are similar to recipes you find on a food blog except
in reverse. The story about why you might want to make Nanna's secret
apple pie ice cream comes first in a food blog. It helps set the scene
for why people care.

In Technical recipes, people don't need to be convinced that they need
help; that's why they are reading your recipe. They need to understand
why your solution is the best approach.

#### An example of a technical recipe: 

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="configuring-the-router-via-tftp">Configuring the router via TFTP</h2>
<h5 id="problem">Problem:</h5>
<p>You want to load configuration commands via TFTP.</p>
<h5 id="solution">Solution:</h5>
<p>You can use copy tftp: command to configure the router via the Trivial Fire Transfer Protocol (TFTP)</p>
<p><img src="C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image5.png" style="width:5.83194in;height:2.26875in" /></p>
<h5 id="discussion">Discussion:</h5>
<p>Generally, most people configure their routers by using telnet/ssh and the configure terminal command. However, for large configuration changes people tend to resort to cutting and pasting a large set of commands. While this method works, it is inefficient and slow, particularly if you have to configure a large number of routers. </p>
<p>Using TFTP to download a large set of configuration commands, the router doesn’t need to echo each character to your screen, which reduces the overhead and increase the speed of the interaction. </p>
<p>In this example, the router is configured by downloading a file called NEWCONFIG from a server at 192.168.10.1 by using the Trivial File Transfer Protocol (TFTP). The router will copy the entire file by TFTP before entering the commands into the running configuration. </p>
<p>This is useful because sometimes some commands in the middle of a configuration could disrupt your access to the router, but the rest of the commands might fix the problem. If you tried to enter them manually using telnet/ssh and configure terminal, you could simply lock yourself out of the router. A typical example of this problem happens when you replace an active access-list. When you enter the first line the router puts an implicit deny all at the end which can break your session. Using TFTP avoids this problem.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Challenge Response

Lastly, you must submit the response to the Networking Challenge issued
as a part of your Labs. This challenge-response will require the
subnetting calculations and Network Configuration for the following
Network

![Diagram, schematic Description automatically
generated](C:\Users\carte\Desktop\github\IT-CBR\assignments\Network Administration and Security/media/image6.png){width="6.268055555555556in"
height="3.7930555555555556in"}

NOTE: This network is incomplete and will be updated early this week.

## Rubric

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 45%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
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
<td><p><strong>Cookbook</strong></p>
<p>(individual)</p></td>
<td><p>You have submitted evidence of completing a cookbook which contains three recipies. Each recipe makes clear that you have made a serious attempt to complete the assignment within the spirit that it is offered. Your three selected recipies make clear that they are likely to be useful for you and show examples of analysis/evaluation/comparison/contrasting.</p>
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
<td>__/ 6</td>
</tr>
<tr class="odd">
<td><p><strong>Subnet Tables</strong></p>
<p>(individual)</p></td>
<td><p>You have submitted evidence of calculting the subnetting requirements of your two business networks.</p>
<p>The evidence supplied shows that you have submitted work in good faith to the spirit of the assignment and makes clear that calculations are produced to likely be correct.</p></td>
<td>2</td>
<td>__/2</td>
<td>__/2</td>
<td>-</td>
<td>__/ 2</td>
</tr>
<tr class="even">
<td><p><strong>Challenge Response</strong></p>
<p>(individual)</p></td>
<td><p>You have submitted evidence of completing your challenge response. Your challenge response shows evidence of design challenge:</p>
<ul>
<li><p>Two business networks each connected via switch networks with a local DHCP and DNS server that allocate IP addresses.</p></li>
<li><p>Subnetted with each subnet connected via serial.</p></li>
<li><p>Connected to the internet and can reach services</p></li>
</ul>
<p>You have supplied evidence that each of these domains work appropriately in a test environment. This includes pinging relative services and demonstration of reaching services such as web access to facebook.com and cisco.com</p>
<p>Evidence for knowledge, comprehension, and application may include:</p>
<ul>
<li><p><strong>Knowledge</strong>: Your evidence highlights that you recall and list relevant terms in your learning. It may tell a story to the reader (the teacher) or state the conditions of your learning.</p></li>
<li><p><strong>Comprehension</strong>: Your evidence highlights that you can identify critical aspects of your learning or explain what you've done to the author.</p></li>
<li><p><strong>Application</strong>: It is clear from your evidence that you constructed a complete submission</p></li>
</ul>
<p>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</p></td>
<td>2</td>
<td>__/2</td>
<td>__/2</td>
<td>-</td>
<td>__/ 2</td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Analysis, Synthesis &amp; Evaluation</strong></td>
<td colspan="2"></td>
<td colspan="2"><strong>SUB TOTAL</strong></td>
<td><strong>__ / 14</strong></td>
</tr>
<tr class="even">
<td><strong>Cookbook recipies</strong></td>
<td>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td>-</td>
<td>__ / 4</td>
</tr>
<tr class="odd">
<td><strong>Challenge Response</strong></td>
<td>Note: the assessor may use their discretion to source other evidence from this assessment to judge the activity if required.</td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td>-</td>
<td>__ / 4</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Submission Guidelines</strong></td>
<td colspan="2"></td>
<td colspan="2"><strong>SUB TOTAL</strong></td>
<td><p><strong>A __/12</strong></p>
<p><strong>T __/24</strong></p></td>
</tr>
<tr class="odd">
<td><strong>Submitability</strong></td>
<td><strong>Assessment submission is ordered</strong> and has a definite pattern to its construction. <strong>The reader is not confused about the content in any given section and can follow the submission flow</strong> easily. </td>
<td>4</td>
<td>__/4</td>
<td>__/4</td>
<td>-</td>
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
<td><strong>A __/32<br />
T __/44</strong></td>
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
