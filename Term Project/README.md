
#Exploring Anti-Cancer Drug Testing via Critical Path

Northwestern University MSDS 460 Term Assignment


## Abstract
In the context of drug development and discovery, researchers are able to utilize national
federal resource supercomputers to find non biologic lead compounds able to target druggable
cancer cells. Without the use of AI scientists take weeks
to come up with 5 lead chemical compounds but, with AI driven models and the use of
supercomputers scientists are able to have billions of possibilities offered to them in one hour.
This computational stage of drug discovery is costly and requires funding via grant awards. The
primary objective is to secure additional grant funding by demonstrating a systematic approach
to document and forecast a percentage to completion of the drug development process. The
proposed method involves a meticulous examination of the critical path, emphasizing efficiency
in the development process. This analysis is not merely procedural but serves as a strategic tool
to provide stakeholders and funding entities with a quantifiable measure of progress. By
scrutinizing the critical path and forecasting the percentage to completion, they seek to present a
transparent and measurable account of their efficiency in the drug development process. This
methodical assessment serves as a basis for decision-makers to evaluate the project's
advancements and allocate resources accordingly.
## Methodology
The main driver of this project will be a critical path analysis; this will be especially
useful since there are several different processes in anti-cancer drug development that help
convert raw materials into finished goods. Because these processes are highly regulated, there
are specific components that each drug must interact with, ranging from structural analysis to
animal testing to clinical trials.1 To complete this task, it is important to acknowledge the
duration and dependencies of each activity, while also considering logical endpoints.
Additionally, we will provide considerations for best and worst case scenarios with a specific
margin of error. The tasks and dependencies will also be modeled in a table, and the final figure
will be a comprehensive map for anti-cancer drug development. Overall, the end result will
provide the research team with a single path in deterministic processing times.

The code to solve this real-world problem is an implementation of a linear programming
(LP) model to find the critical path in a project scheduling problem code and outcomes are
available on this Github repository:
https://github.com/hheid-huc/MSDS460_Group_Assignments/tree/main/Term%20Project.

First, the code creates an ‘expected_tasks’ dictionary, specifying the expected duration
and cost for each task. Next, task dependencies are outlined in the ‘precedences’ dictionary. The
linear programming problem is formulated using the ‘pulp’ library, creating decision variables
for the start and end times of each task. Constraints are established to ensure that the end time of
each task is equal to its start time plus its expected duration, and that the start time of each task is
greater than or equal to the end time of its predecessors. The objective function is designed to
minimize the total project duration, expressed as the sum of end times for all tasks. The code
then solves the linear programming problem to find the optimal solution. Results are printed,
including the critical path time for expected time estimates, start and end times for each task, and
the solution variable values. In essence, this code provides a systematic approach to project
scheduling by employing linear programming techniques, aiding in the identification of the
critical path and the overall duration of the project based on given task dependencies and
expected durations.

1 See Appendix A.1 for Task Table
## Results
For the expected, best, and worst case scenarios the critical pathways were all the same. It
was done in the following order of operations: Target Identification, Test Libraries Created,
Failures go Back to Refine the Computational Model, and Hire Synthetic Chemists to Make
Market Compounds.2 The critical path essentially identifies the sequence in which tasks need to
be completed on time in order for the project to run as planned. At the same time, the critical
path is the longest path that can be taken and is impacted by any delays in tasks. The results
obtained from this critical path analysis are based on estimates for a proof of completion for a
grant proposal. For the expected scenario, the percentages completed for each task as listed
above in order is as follows: 105%, 102%, 200%, and 100%. The percentages are calculated by
taking the actual duration of the task and dividing it by the planned duration (which can be
extracted from the expected duration portion of the code), then multiplying by 100. This
indicates that the project is progressing much faster than anticipated and could be an indication
of efficient progress.

For the worst case scenario, the percentages completed for each task in the order of
Target Identification, Test Libraries Created, Failures go Back to Refine the Computational
Model, and Hire Synthetic Chemist to Make Market Compounds were all 100%. This again
indicates that even in the worst case scenario, the critical pathway tasks were still able to be
completed within the pessimistic time frame, without any delays or unforeseen issues. This could
also indicate that the estimates were accurate and the team was able to execute the tasks within
the restrictive time frame.

For the best case scenario, the percentage completion rate for Target Identification was
130%, Test Libraries Created was 120%, Failures go Back to Refine the Computational Model
was 500%, and Hire Synthetic Chemist to Make Market Compounds was 170%. Being well over
100% completed, the optimistic estimates expect task completion to go exceptionally well. This
could be due to numerous factors such as efficient execution, excellent management and resource
allocation, early completion, successful risk mitigation, or even less slack/obstacles than
anticipated.

Within a well managed project, the percentage completion rate of tasks should be
expected to be close to 100%. Since the critical path determines the sequence of tasks that define
the entire project, the tasks on the critical path have no room to delay as this would directly affect
the project completion rate. With task completion percentages all being 100% or over, this
indicates that the project is running according to schedule and most likely is not experiencing
any delays. The critical pathway also is associated with high-priority tasks, meaning that
successful management of task completion is vital to ensuring the success of the project. For the project at hand, a critical pathway allows researchers to better understand the
expectations that can be met during the drug development process. By implementing the resource
of AI models, researchers are more likely to secure grant funding by depicting a process of
efficiency via the percentage completed of tasks(You et al, 2023). Having quantifiable
measurements to exhibit the progress made allows decision-makers to effectively allocate
resources as needed.

2 See Appendix A.2 for Network Diagram

## Bibliography
Chace, Calum. “First Wholly      AI-Developed Drug Enters Phase 1 Trials.” Forbes, October 5,
2023.
https://www.forbes.com/sites/calumchace/2022/02/25/first-wholly-ai-developed-drug-enter
s-phase-1-trials/?sh=54828dcf2680.
Wang, Liuying, Yongzhen Song, Hesong Wang, Xuan Zhang, Meng Wang, Jia He, Shuang Li,
Liuchao Zhang, Kang Li, and Lei Cao. “Advances of Artificial Intelligence in Anti-Cancer
Drug Design: A Review of the Past Decade.” Pharmaceuticals (Basel, Switzerland),
February 7, 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9963982/.
You, Yujie, Xin Lai, Yi Pan, Huiru Zheng, Julio Vera, Suran Liu, Senyi Deng, and Le Zhang.
“Artificial Intelligence in Cancer Target Identification and Drug Discovery.” Nature News,
May 10, 2022. https://www.nature.com/articles/s41392-022-00994-0.
Miller, W. Thomas. “Williams-Critical-Path Analysis.py” 2023.
https://canvas.northwestern.edu/courses/200718/assignments/1276266?module_item_id=
2761717
## Appendix


![Figure A.1 Drug Discovery Tasks, Dependencies, and Estimates](https://drive.google.com/uc?id=13guJKrFY_ib2Ce9UuuqrqlXFWGkpGWQ4)
Figure A.1 Drug Discovery Tasks, Dependencies, and Estimates



![Figure A.2 Critical Path Diagram](https://drive.google.com/uc?id=1ZthPh49RS5X4NjP8ls_bkXEz6ZpGnXu0)
Figure A.2 Critical Path Diagram


![Figure B.1](http://drive.google.com/uc?id=1wG1fmGc87DFasZp0cP9hOhkyiAwFpmtK)
Figure B.1 Gantt Chart depicting the duration in hours for expected outcome scenario with percentage completed error bars for critical pathways.


![Figure C.1](http://drive.google.com/uc?id=1N76Rl5xb-QO7ETRdvhhv6otDSK6rhfag)
Figure C.1 Gantt Chart depicting the duration in hours for the worst case outcome scenario with percentage completed error bars for critical pathways. 



![Figure C.1](http://drive.google.com/uc?id=1OC_GqSlRSFwuwpjfSSP9rZTBJ1KIQetg)
Figure D.1  Gantt Chart depicting the duration in hours for best outcome scenario with percentage completed error bars for critical pathways. 

