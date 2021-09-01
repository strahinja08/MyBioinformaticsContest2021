# MyBioinformaticsContest2021

This code is used in prefinals (qualification phase). 
Each directory contains run script that reads the file from the same directory, 
The sample and test data are given during the competition.

Run the ```python <script>.py``` cmd, after ensuring that the appropriate test data is hardcoded in the <script>.py
  
  
  
Assignment description (copyright@Stepik):
  
  
  """
  Diagnosis
Determining the correct diagnosis is a crucial step in patient treatment. However, it can be far from trivial, as the disease can have multiple phenotypic manifestations with different degrees of specificity, partly overlapping with other conditions. To formalize the diagnostics process, Human Phenotype Ontology (HPO) was invented, using which both the disease manifestations and patient phenotypic traits can be described. In this problem, your task will be to identify the patients' diseases given their clinical phenotypes.

In this problem, you are given a human phenotype tree. Each vertex of this tree corresponds to a phenotypic abnormality. The abnormalities on the lower levels are more specific, with the specificity of the vertex vv defined as information content \textit{IC}(v)IC(v) value. Additionally, you are given descriptions of several diseases, each defined as a set of abnormalities, that is vertices of the phenotype tree. Finally, you are given descriptions of patients, similarly defined as sets of phenotype tree vertices, describing their clinical phenotypes.

Your task is to find for each of the patients their most likely disease. More precisely, for every patient pp with the phenotype set Q_pQ 
p
​	
  find the disease mm with the phenotype set D_mD 
m
​	
  which maximizes the value of

\sum_{q \in Q_p} \Big( \max_{d \in D_m}\textit{IC}\big(\textit{LCA}(q, d)\big) \Big),
q∈Q 
p
​	
 
∑
​	
 ( 
d∈D 
m
​	
 
max
​	
 IC(LCA(q,d))),
where \textit{LCA}(q, d)LCA(q,d) is the lowest common ancestor of phenotype vertex qq and phenotype vertex dd and \textit{IC}(v)IC(v) is the information content of vertex vv. If there are several diseases with the same maximal value, then any of them can be returned.

Input Format
The first line of the input file contains one integer nn — the number of vertices in the phenotype tree. The vertices are identified by numbers 1, 2, \ldots, n1,2,…,n, with vertex 11 being the root of the tree.

The second line contains n - 1n−1 integers — the parent identifiers for the vertices 2, 3, \ldots, n2,3,…,n.

The third line contains nn integers — information content values of the corresponding vertices 1, 2, \ldots, n1,2,…,n. It is guaranteed that for every vertex vv its information content \textit{IC}(v)IC(v) is greater than the information content of its parent vertex.

The fourth line contains one integer mm — the number of diseases.

Next mm lines contain descriptions of diseases. The ii-th line contains an integer cm_icm 
i
​	
 — the number of vertices in the phenotypes tree describing the ii-th disease, followed by cm_icm 
i
​	
  different integers — the identifiers of vertices describing the ii-th disease.

The next line contains one integer nqnq — the number of patients.

Next nqnq lines contain descriptions of patients. The ii-th line contains an integer cq_icq 
i
​	
 — the number of vertices in the phenotypes tree describing the ii-th patient, followed by cq_icq 
i
​	
  different integers — the identifiers of vertices describing the ii-th patient.

Output Format
The output file should contain nqnq lines. The ii-th line should contain one integer — the identifier of a disease of the ii-th patient. The indexing starts from 1.

Scoring
For all tests, you will receive points proportional to the number of diseases you recovered correctly.
  
  """
