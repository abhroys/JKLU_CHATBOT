import re

# Sample input text (Paste your text here)
input_text = """
2021
Title of paper	Name of the author/s	Name of journal	Year of publication	ISSN number
Cost inspection of a Geo/G/1 retrial model using particle swarm optimization and Genetic algorithm	Malik, G., Upadhyaya, S.  and Sharma, R	AIN Shams Engineering Journal	2021	ISSN: 2090-4479
Analysis of Heterogeneous Data Storage and Access Control Management for Cloud Computing under M/M/c Queueing Model	Divya Sharma, Gireesh Kumar and Richa Sharma	International Journal of Cloud Applications and Computing (IJCAC)	2021	2156-1834
Vertical Bearing Behavior of Monopod Caisson Foundation in Sandy Soils	Tanmoy Kumar Deb and Baleshwar Singh	Journal of Waterway, Port, Coastal, and Ocean Engineering	2021	0733-950X
Design of Flexible Tactile Array Sensor	Devika Kataria, Gustavo Sanchez, Jyoti Prakash Naidu and Mandayam A. Srinivasan	IETE Journal of Research	2021	0377-2063
ANFIS Model to Predict Effect of Tool Pin Length and Position on Tensile Strength of Friction Stir Welded Joint	Deepika Mishra, Ravi Shankar Prasad and Sudhir Kumar	Welding International	2021	0950-7116
Hydro Power Potential from Low Head Irrigation Reservoirs: A Case Study of Rajasthan	Kedar Sharma and Shubham Bajaj	Water and Energy International	2021	0974-4207
Corporate Social Responsibility and Sustainable Development Goals: A Study of Indian Companies	Lokanath Mishra	Journal of Public Affairs	2021	1479-1854
Covid Time: Fintech as an Alternative to Banking Operations	Mishra L, Joshi N & Saxena S.	Shodh Sanchar Bulletin, Vol 11, Issue 41	2021	2229-3620
Analyzing Emergent Complexity in Particle Swarm Optimization using a Rolling Technique for Updating Hyperparameter Coefficients	Amit Sethi and Devika Kataria	Procedia Computer Science,193, pp.513-523, 2021	2021	1877-0509
Investigation of Functionally Graded Adherents on Failure of Socket Joint of FRP Composite Tubes	Prakash, Chander, Vidyapati Kumar, Ankita Mistri, Amrinder S. Uppal, Atul Babbar, Bhargav P. Pathri, Jonty Mago, Ankit Sharma, Sunpreet Singh, Linda Y. Wu, and Hongyu Zheng	Materials 14, no. 21: 6365	2021	1996-1944
Medical Data Clustering and Classification Using TLBO and Machine Learning
Algorithms	Ashutosh Kumar Dubey, Umesh Gupta, and Sonal Jain	Computers,Materials & Continua, 2022, vol.70, no.3, pp.4523-4543	2021	1546-2226
HIL Investigations on Intelligently Tuned PV Integrated DSTATCOM to Enhance Power Quality	Agrawal HP, Bansal HO, Kumar R and Sisodia YS	Arabian Journal for Science and Engineering, 2021	2021	2191-4281
Detailed Survey and Discussion on Data and Document Security Concerns in Cloud Computing: Moving from Single cloud to Multi-Clouds	Chintal Patel, Amit Sinhal	Design Engineering,  VOL 21: ISSUE 06, pp8067- 8076	2021	0011-9342
The Impact of Green Practices on the Financial Performance: A study of MSMEs	V. Shruti & Mundra S.	Shodh Sanchar Bulletin, Vol 11, Issue 41, Jan- March 2021	2021	2229-3620
Eldercare helpline: connecting with older people to mitigate the effects of the Covid-19 crisis in Jaipur, India	Raina, R.L., Gupta, A., Gupta, U., Singh, U. and Jain, D.	Working with Older People,	2021	1366-3666
Market Backwardation and The Theory of Storage: An Empirical Investigation of Indian Gold Futures Markets.	Nair, J. R., Kumar, B., & Inani, S.	Global Business Review	2021	097215092110463
2020
Title of paper	Name of the author/s	Name of journal	Year of publication	ISSN number
Fundamentals of Automation Engineering: A hybrid project-based learning approach	Devika Kataria , Gustavo Sanchez
and Siddhartan Govindasamy	International Journal of Electrical Engineering
& Education	2020	ISSN: 0020-7209
Performance Analysis of Solar Operated Milk Refrigerator Using R290	Kasera, Shailendra, Nayak, Rajlakshmi, and Bhaduri, Shishir Chandra	International Conference on Innovations in Thermo-Fluid Engineering and Sciences, NIT Rourkela, Feb 10-12, 2020	2020	 
An Anlytical and Economical Assessment of the Waste Cooking Oil based Biodiesel using Optimized Conditions on the Process Variables	Ashish Dubey, Ravi Shankar Prasad and Jitendra Kumar Singh	Energy Sources, Part A: Recovery, Utilization, and Environmental Effects	2020	1556-7036
The Highly Secure Polynomial Pool-based Key Pre-Distribution Scheme for Wireless Sensor Network	Vishal Choudhary and Sunil Taruna	Journal of Discrete Mathematical Sciences and Cryptography	2020	0972-0529
Fuzzy Logic Controller and Game Theory based Distributed Energy Resources Allocation	Akash Talwariya, Pushpendra Singh	AIMS Energy	2020	 
Multifunctional biogenically synthesized porous multi-walled carbon nanotubes dispersed polymer electrolyte-based supercapacitor	Rachana Ranu, Yatishwar Chauhan, Amar Ratan, Swati Yadav and Sandeep Kumar Tomar	Applied Physics A: Materials Science and Processing	2020	0947-8396
Electrical defects in m-MTDATA studied using charge transient spectroscopy	K Sudheendra Rao, Devika Kataria and  Durgesh C.Tripathi	Materials Today: Proceedings	2020	ISSN: 2214-7853
Study of the open circuit voltage dependence on incident light intensity of planar heterojunction organic solar cell	Anukul Prasad Parhi, Durgesh C.Tripathi and DevikaKataria	Materials Today: Proceedings	2020	ISSN: 2214-7853
Spectral Clustering and Cost-Sensitive Deep Neural Network-Based Undersampling Approach for P2P Lending Data	Jadwal, P. K., Jain, S., & Agarwal, B.	International Journal of Information Technology and Web Engineering (IJITWE), 15(4)	2020	ISSN: 1554-1045
Biometric finger print based voting machine using ATmega328P microcontroller	Kanwardeep Singh Gehlot, Divanshu Jain	Materials Today: Proceedings	2020	ISSN 2214-7853
Semiconductor chip designing strategic necessity for India	 Milind Thomas Themalil	Dataquest	Apr-20	 
Simple Marketing Strategies for Promoting
Library Resources and Services	Laxmi Chand Sharma and Mukesh Pathak	Informatics Studies, Vol. 7, Issue 4	Oct-20	ISSN 2320 – 530x
Stackelberg Game Theory Based Energy Management Systems in the Presence of
Renewable Energy Sources	Akash Talwariyaa, Pushpendra Singha and Mohan Lal Kolheb	IETE Journal of Research, Vol 67, Issue 1	2020	 
An analysis of batting performance of the cricket players	Harshita Khangarot and Alok Kumar	International Journal of Advanced Science and Technology	2020	2005-4238
An ANFIS Model for Study of Surface Roughness for Metallic Materials on Optimized Machining Parameters	Deepika Mishra, Ravi Shankar Prasad, Mohd Zubair, and Piyush Gaur	Arctic	2020	0004-0843
Geometric Properties for an Unified Class of Functions Characterized Using Fractional Ruscheweyh-Goyal Derivative Operator	Ritu Agarwal, Gauri Shankar Paliwal, and Sunil Dutt Purohit	Science and Technology Asia	2020	2586-9000
Data Analytics for Substation Overloading Assessment of Solar Integrated Distribution System	Jagdish Prasad Sharma	International Journal of Recent Technology and Engineering (IJRTE)	2020	2277-3878
Assessment of Hydro Power Potential from Low Head Irrigation Reservoirs: A Case Study of Rajasthan, India	Kedar Sharma and Shubham Bajaj	Water and Energy International	2020	0974-4207
A Review of Literature and Netnography based Approach to Exploring and Investigating the Antecedents of Brand Avoidance	Ajay Singh Chandel and Punam Mishra	Shodh Sarita	2020	2348-2397
Exploring and Investigating Antecedents of Brand Avoidance	Ajay Singh Chandel and Punam Mishra	Shodh Sarita	2020	2348-2397
Estimation of stress-strength reliability based on skew Logistic distribution	Gupta, Jaya , Garg, Mridula and Singh, Chandarmohan	Journal of Rajasthan Academy of Physical Sciences	2020	ISSN: 0972-6306
Robert Frost’s Theme of Alienation	Vijaylakshmi and Praveen Bala	International Journal of Advanced Science and Technology	2020	2005-4238
Particle Swarm Optimization and Maximum Entropy Results for MX/G/1 Retrial G-Queue with Delayed Repair	Malik, G., Upadhyaya, S.  and Sharma, R	International Journal of Mathematical, Engineering and Management Sciences, Vol. 6, No 2	2020	ISSN: 2455-7749
2019
Title of paper	Name of the author/s	Name of journal	Year of publication	ISSN number
A Priority Based - Weighted Clustering Algorithm for Mobile Ad Hoc Network	Pathak, Sunil, and Jain, Sonal	International Journal of Communication Networks and Distributed Systems, 2019	2019	ISSN: 1754-3916
Clustered Support Vector Machine for ATM Cash Repository Prediction.	Jadwal P.K., Jain S., Gupta U., Khanna P.	Advances in Intelligent Systems and Computing, vol 713. Springer, Singapore	2019	 
Generalization of Taylor’s Formula and Differential Transform Method for Composite Fractional q-derivative	Chanchalani, Lata, Subhash Alha, and Jaya Gupta,	The Ramanujan Journal 48, (2019): 21–32.	2019	 
JavaRelationshipGraphs (JRG): Transforming Java Projects into Graphs using Neo4j Graph Databases	Arora, Ritu, and Goel, Sanjay	International Conference on Software Engineering and Information Management, 80-84. Bali, Indonesia: ACM New York, USA	2019	 
Development of Fuzzy Logic Controller for Photovoltaic Integrated Shunt Active Power Filter	Kumar, Ravinder, Bansal, Hari Om, and Agrawal, Hanuman Prasad	Journal of Intelligent & Fuzzy Systems 36, 6(2019): 6231-6243.	2019	 
Biodegradation of Sludge Produced from Common Effluent Treatment Plant (CETP) Using Drum Composting Technique	Maheshwari, Seema, Jethoo, Ajay Singh, Vishvakarma, Vinod Kumar, Meena, Khwairakpam	International Journal of Nature Environment and Pollution Technology 18, 1 (2019): 231-236.	2019	 
A stepwise power tariff model with game theory based on Monte-Carlo simulation and its applications for household, agricultural, commercial and industrial consumers	Akash Talwariya, Pushpendra Singh, Mohan Kolhe	International Journal of Electrical Power & Energy Systems (Elsevier-SCI Journal) , Volume 111, April 2019, Pages 14-24.	2019	 
A Game Theory Approach for Energy Tariff and Demand Side Management	A. Talwariya, S.K. Sharma, P. Singh and M. Kolhe	IEEE International Conference on Recent Advancement and Innovations in Engineering (ICRAIE), Jaipur Published on IEEE Xplorer May 2019.	2019	 
Consumer Activism and the Advent of Online Anti Brand Communities: A Netnographic Analysis	Mishra, Punam, and Ajay Chandel	AIMS Journal of Management 4, No.2(2019): 222-233.	2019	 
Investigation of Fatigue Crack Propagation in Adhesively Bonded Joints Using Fatigue Testing, Finite Element Analysis and Neural Networks	Gaur, P and Prasad, R S	Applied Engineering Letters 4, 4 (December 2019): 136-149.	2019	 
Computational Measure of Cancer Using Data Mining and Optimization	Dubey, Ashuosh Kumar, Gupta, Umesh and Jain, Sonal	Data Engineering and Communications Technologies 39, Springer, Cham: 626-632.	2019	 
Design Thinking in Startups - A Case Study on Car Dhulao	Gupta, Umesh and Mundra, Sheetal	SHODH-AMRIT: JKLU Journal of Engineering & Management 2, 1 (2019): 212-215.	2019	 
Availability Modelling of Cluster-Based System with Software Aging and Optional Rejuvenation Policy	Sharma, R. and Kumar, G	Cybernetics and Information Technologies 19, 4(2019): 90-100.	2019	 
Identifying Major Death Causing Disease using Decision Tree based Death Analysis	Jaju, H. and Sharma, R	SHODH-AMRIT: JKLU Journal of Engineering & Management 2, 2 (2019): 1-19	2019	 
Multi-Criteria Pareto-Based Control Loop Performance Assessment	Gustavo Sanchez	IEEE International Conference on Recent Developments in Control, Automation and Power Engineering at Amity University, Noida (India) during October 10-11, 2019.	2019	 
process optimization for energy consumption and salt removal in vacuum membrane distillation for desalination	Jitendra Kumar Singh	Department of Chemical Engineering, Malaviya National Institute of Technology Jaipur and NIT Uttrakhand, during 28-29 December 2019.	2019	 
Investigation of Fatigue Crack Propagation in Adhesively Bonded Joints Using Fatigue Testing, Finite Element Analysis and Neural Networks	P Gaur, R S Prasad	Applied Engineering Letters, Vol. 4(4), December 2019, pp 136-149.	2019	 
Availability Modelling of Cluster-Based System with Software Aging and Optional Rejuvenation Policy	Sharma, R. and Kumar, G	Cybernetics and Information Technologies, Vol. 19, No 4, pp. 90-100, DOI: 10.2478/cait-2019-0038	2019	 
Reliability Analysis of Software with Three Types of Errors and Imperfect Debugging using Markov Model	Kumar G., Kaushik M. and Purohit R	International Journal of Computer Applications in Technology, Vol 58, No. 3, pp. 241-249	2019	 
A smart manufacturing adoption framework for SMEs.	Mittal, S., Khan, M. A., Purohit, J. K., Menon, K., Romero, D., & Wuest, T	International Journal of Production Research, 1-19	2019	 
Smart manufacturing: characteristics, technologies and enabling factors	Mittal, S., Khan, M. A., Romero, D., & Wuest, T.	Journal of Engineering Manufacture, 233(5), 1342-1361	2019	 
Impact of IIoT based technologies on characteristic features and related options of nonownership business models	Menon, K., Mittal, S., Kärkkäinen, H., & Wuest, T	International Conference on Product Lifecycle Management, 8-12	2019	 
Building Blocks for Adopting Smart Manufacturing	Mittal, S., Khan, M. A., Romero, D., & Wuest, T	Procedia Manufacturing, 34, 978-985	2019	 
Maximum power point tracking in wind energy conversion system using radial basis function based neural network control strategy	Ravinder Kumara, Hanuman Prasad Agrawalc, Aakash Shaha,b, Hari Om Bansal	Elsevier Sustainable Energy Technologies and Assessments 36 (2019) 100533	2019	 
Night Driving Safety: Automatic Headlight Beam Adjuster	K. Gahlot, D. Jain	International conference on Innovations in Technology and Management for Achieving Sustainable Development Goals (SDGs)	2019	 
Li-Fi: A Solution for reducing the Impact of Electromagnetic Radiation on Human Health	K. Gahlot, H. Gupta, D. Jain	International conference on Innovations in Technology and Management for Achieving Sustainable Development Goals (SDGs)	2019	 
Regression approach to power Transformer health assessment using health index	J.P. Sharma	International Conference on Emerging Trends in Electro-Mechanical Technologies and Management	2019	 
An Enhanced Proxy Server for Better Performance & Security of Network for Academics	Dangi, Rahul, Jha, Varun Kumar, Choudhary, Manoj and Bhavsar, Devendra	International Journal of Research in Advent Technology (IJRAT) 7, 6S (2019): 278-281	2019	 
Computational Measure of Cancer Using Data Mining and Optimization	Dubey, Ashutosh Kumar, Gupta, Umesh and Jain, Sonal	Data Engineering and Communications Technologies 39, Springer, Cham: 626-632.	2019	 
Investigation of Fatigue Crack Propagation in Adhesively Bonded Joints Using Fatigue Testing, Finite Element Analysis and Neural Networks	Gaur, P and Prasad, R S	Applied Engineering Letters 4, 4 (December 2019): 136-149.	2019	 
Clustering of Water Reservoirs based on Water Chemical Analysis	Gupta, Umesh, Jain, Sonal, Kumawat, Dharmendra and Sharma, Roopali	International Journal of Research in Advent Technology (IJRAT) 7, 6S (2019): 274-277.	2019	 
Design Thinking in Startups - A Case Study on Car Dhulao	Gupta, Umesh and Mundra, Sheetal	SHODH-AMRIT: JKLU Journal of Engineering & Management 2, 1 (2019): 212-215	2019	 
A Comprehensive Study on the Development of Smart Cities in India from a Computer Science & Engineering Perspective - keeping in view the UN SDGs	Jain, Muskaan, Arora, Rashi and Vyas, Abhishek	International Journal of Research in Advent Technology (IJRAT) 7, 6S (2019): 227-231.	2019	 
Identifying Major Death Causing Disease using Decision Tree based Death Analysis	Jaju, H. and Sharma, Richa	SHODH-AMRIT: JKLU Journal of Engineering & Management 2, 2 (2019): 1-19	2019	 
Energy Evaluation Performance of Variable Speed Solar Milk Refrigerator using R290	Kasera, Shailendra, Nayak, Rajlakshmi, and Bhaduri, Shishir Chandra	International Conference on “New and Renewable Energy Resources for Sustainable Future", SKIT, Jaipur. Nov 4-7, 2019	2019	 
Smart Hydroponic System	Purwar, Shreyash, Bhatt, Anudit, and Kataria, Devika	International Journal of Research in Advent Technology (IJRAT) 7, 6S (2019): 282-285.	2019	 
Upgrading Higher Education to Produce, Nurture & Groom Students as Successful Professionals	Raina, R. L. and Ghosh, Pratistha	An Approach at JK Lakshmipat University (JKLU). University News 57, 49 (December 2019): 47-52.	2019	 
Analysis of Signals in Communication System under Buffer Handover Scheme: A Queuing Approach	Rohit and Sharma, Richa	 International Journal of Computer Science Engineering 08, 4(2019): 129-136.	2019	 
Effect of rGO Concentration on the Thermal Stability of PANI/rGO Nano-composites	Sharma, Ajay Kumar, Jain, Praveen Kumar, Vyas, Rishi, Mathur, Vishal, and Jain, Vipin Kumar	Journal of Nano and Electronic Physics 11, 5 (2019): 05042	2019	 
Enhanced Optical and Dielectric Properties of PANI/rGO Nanocomposites for Supercapacitor Application	Sharma, Ajay Kumar, Jain, Praveen Kumar, Vyas, Rishi, Mathur, Vishal, and Jain, Vipin Kumar	Journal of Nano and Electronic Physics 11, 5 (2019): 05026	2019	 
Availability Modelling of Cluster-Based System with Software Aging and Optional Rejuvenation Policy	Sharma, Richa and Kumar, Gireesh	Cybernetics and Information Technologies 19, 4(2019): 90-100.	2019	 
Sustainable Development Goals: Contribution of Higher Education	Singh, Shikha and Mundra, Sheeta	International Journal of Research in Advent Technology (IJRAT) 7, 6S (2019): 270-273.	2019	 
Energy Efficient Computing for Smart Phones in Cloud Assisted Environment	Arya, N., Choudhary, S., & Taruna, S	International Journal of Computer Networks & Communications (IJCNC) Vol.11, No.5, September 2019	2019	 
Research based and Design based Education: Experiences in India	Jyoti Prakash Naidu	Engineering Conference (IDETC/CIE2019). ASME, Anaheim, California, USA: August 18-21, 2019	2019	 
Comparative study on assessment of compost stability through C/N ratio by different composting techniques	Vinod Kumar Vishwakarma	International Conference on Academic Research in Science, Technology and Engineering (ICARSTE-2019). Sapienza University of Rome, Italy: May 10-12, 2019	2019	 
Multi-Criteria Pareto-Based Control Loop Performance Assessment	Gustavo Sanchez	3rd IEEE International Conference on Recent Developments in Control, Automation and Power Engineering at Amity University, Noida (India) during October 10-11, 2019	2019	 
An Overview of Stone and Marble Industry of Rajasthan with Life Cycle Analysis and Industrial Survey	Prajwal, B., Mali, H. S., and Nagar, R	 Journal on Economics & Commerce, 1(1), 38-56.	2019	 
The Determinants of Reverse Mortgage Choice of Indian Elderly Homeowners for Sustainable Livelihood: A Logit Analysis	Gupta, S., & Kumar, S	Humanities & Social Sciences Reviews, 7 (4), 309-317	2019	 
Economic Factors Influencing Indian Older Homeowners' Decision to Opt for Reverse Mortgage: An Empirical Investigation	Gupta, S., & Kumar, S	IUP Journal of Management Research, 18(3), 25-38	2019	 
Housing Wealth Dissaving Choices of Indian Urban Homeowners in Later Life: Influence of Uncertain Life Span and Demographics	Gupta, S., & Kumar, S	IUP Journal of Applied Finance, 24(4), 48-68	2019	 
An Overview of Stone and Marble Industry Of Rajasthan With Life Cycle Analysis And Industrial Survey	Bhargav Prajwal, Harlal Singh Mali,	Journal on Economics & Commerce	2019	 
Development of fuzzy logic controller for photovoltaic integrated shunt active power filter	R. Kumar, H.O. Bansal and H.P. Agrawal	Journal of Intelligent & Fuzzy Systems, Volume 36, pp. 6231-6243, 2019.	2019	 
Maximum power point tracking in wind energy conversion system using radial basis function based neural network control strategy	R. Kumara, H.P. Agrawal, A. Shaha and H.O. Bansal	Sustainable Energy Technologies and Assessments (Elsevier), Volume 36, pp. 1-10, 2019	2019	 
An Enhanced Proxy Server for Better Performance & Security of Network for Academics	Dangi, Rahul, Jha, Varun Kumar, Choudhary, Manoj and Bhavsar, Devendra	International Journal of Research in Advent Technology (IJRAT) 7, 6S	2019	 
Non-cooperative Game Theory Based Stepwise Power Tariff Model using Monte-Carle Simulation for Agricultural Consumers	Akash Talwariya, Pushpendra Singh, Mohan Kolhe	Journal of Open Agriculture, Issue No 4	2019	 
Biogeography Based Optimization Technique for Optimal Siting and Sizing of Distributed Generation System in a Distribution System	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	International Journal of Engineering, Applied and Management Sciences Paradigms (IJEAM)	2019	ISSN: 2320-6608
Optimal siting and sizing of distributed generation system in radial distribution network using particle swarm optimization technique	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	Journal of Emerging Technologies and Innovative Research (JETIR) Vol. 6, Issue 5	2019	ISSN: 2349-5162
An adaptive scheme for Optimal siting of Distributed Generation system in a distribution network	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	International Journal of Recent Technology and Engineering (IJRTE), Vol. 8 Issue 1	2019	ISSN: 2277-3878
A Reverse Power Flow-based Intelligent Protection Scheme for Distributed Generation System	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	Jour of Adv Research in Dynamical & Control Systems	2019	ISSN 1943-023X
Multiple Distributed Generation System Penetration in a Radial Distribution Network	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	International Journal of Engineering and Advanced Technology (IJEAT)	2019	ISSN 2249-8958
Penetration effects of various kinds of distributed generation systems on the distribution system	Amandeep Gill, Surendra Kumar Yadav and Pushpendra Singh	International Journal of Innovative Technology and Exploring Engineering (IJITEE)	2019	ISSN-2278-3075
Optimization of Distribution Networks with Integration of Distributed Generators using Cooperative Game Theory	Akash Talwariya, Pushpendra Singh	International Journal of Power and Energy Systems (Acta Press) Vol 39 (2019)	2019	 
Review of Effective People	Sharma, Ashwini	AIMS Journal of Management 4, No. 2 (2019): 51-52.	2019	 
2018
Title of paper	Name of the author/s	Name of journal	Year of publication	ISSN number
Efficiency of Black and Scholes Model for Pricing Options at Indian Stock Market	Vaibhav Kaushik	Management Dynamics	2018	ISSN No. 0972-5067
Landslide Identification from IRS-P6 LISS-IV Temporal Data - A Comparative Study using Fuzzy based Classifiers.	S. S. Sengar, S. K. Ghosh, A. Kumar and H. Chaudhary	The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences	2018	ISSN 2194-9034 (Online)
Design of MoO3 Buffer Layer for Plasmonic Organic Solar Cell	Devika Kataria and SSK Iyer	Journal of Renewable and Sustainable Energy	2018	ISSN: 1364-0321
Envisioning Post Domain of Restructured Accelerated Power Development and Reforms Programme-Fault Current Limiters	J. P. Sharma and V. Chauhan	Springer Proceedings in Energy	2018	ISSN: 2352-2534
FACT Controllers and their Optimal Location: an Extensive Review	Hanuman Prasad Agrawal and Hariom Bansal	Journal of Engineering Technology	2018	ISSN: 0747-9964
Influence of Solid State Fault Current Limiter on Grid Connected Photo-voltaic System protection	Jagdish Prasad Sharma and H. Ravi Shankar Kamath	Journal of Clean Energy Technologies	2018	ISSN: 1793-821X (Print)
Stochastic voltage stability margin in unbalance feeder with fuzzy based distributed generation placement	Jagdish Prasad Sharma and H. Ravi Shankar Kamath	International Journal of Engineering and Technology (UAE)	2018	ISSN: 2227-524X
Comparative Study of Performance and Emission Characteristics of a CI Engine using Blends of Corn Oil Methyl Ester with Diesel Fuel	Dinesh Kumar Sharma and Ram Kumar Agrawal	International Journal of Renewable Energy Technology	2018	ISSN online 1757-398X ISSN print 1757-3971
Moisture Sensitive Inimitable Armalcolite/PDMS Flexible Sensor: A New E	AshisTripathy, Priyaranjan Sharma, Narayan Sahoo, Sumit Pramanikand Noor Azuan Abu Osma	Sensors and Actuators B: Chemical	2018	ISSN: 0925-4005
Demand Side Management: A Survey of SPT & ToU	Akash Talwariya and Pushpendra Singh	International Journal of Creative Research Thoughts, IJCRT1802214	2018	ISSN: 2320-2882
Smart Grid Developmentin India with Challenges and Opportunities; Execution with Game Theory	Akash Talwariya, Santosh Kumar Sharma, Pushpendra Singh and Mohan Kolhe	International Journal of Technical Research & Science	2018	2454-2024(Online)
Game Theory: Demand Side Management with DG’s and Storage Units	Akash Talwariya, Santosh Kumar Sharma, Pushpendra Singh and Mohan Kolhe	International Journal of Technical Research & Science	2018	ISSN: 2454-2024 EISSN:2454-2024
Level of Confidence in Software Effort Estimation by an Intelligent Fuzzy – Neuro - Genetic Approach	Rijwani, P., and Jain, Sonal	International Journal of Advanced Computer Science and Applications (IJACSA) 9, 9(2018)	2018	ISSN: 21565570, 2158107X
Comparative Study of Online Collaborative Tools for Identification of Effective Tool for Marketing of Products	Anwesha Sinha and S Taruna	International Journal of Computer Applications in Technology 182(18), 14-18, September 2018.	2018	ISSN:0952-8091,    eISSN: 1741-5047
Energy-Efficient Cloud Computing for Smart Phones	N. Arya, S. Chaudhary and S. Taruna	Advances in Intelligent Systems and Computing 1. vol 841. Springer, Singapore, Nov 2018. pp 111-115	2018	ISSN: 2194-5357
The Lomax-Weibull Disribution	Jaya Gupta and Mridula Garg	Advanced Science Letters 1. 24(11), 8126-8129.	2018	ISSN: 1936-6612,  EISSN: 1936-7317
Performance Modeling of Fault Tolerant Machining System with Working Vacation and Working Breakdown	M. Jain, Richa Sharma and R. Meena	Arabian Journal for Science and Engineering 1-12.	2018	ISSN 1319-8025
Impact of Entrepreneurship Education in Graduation Business Start-Up	A. Bansal and Richa Sharma	Organizational Behaviour 121, 51476-51478.	2018	ISSN:1099-1379
Reliability Analysis of Software with hree Types of Errors and Imperfect Debugging using Markov Model	G. Kumar, M. Kaushik and R. Purohit	International Journal of Computer Applications in Technology 182(18), 14-18, September 2018.	2018	ISSN:0952-8091,    eISSN: 1741-5047
Smart Grid Development in India with Challenges and Opportunities; Execution with Game Theory	Akash Talwariya, Santosh Kumar Sharma, Pushpendra Singh & Mohan Lal Kolhe	International Journal of Technical Research & Science (IJTRS) Vol.-3, issue-3	2018	ISSN 2454-2024.
Comparative Study of Clustering Algorithms for MANETs	Pathak, Sunil, and Jain, Sonal	Journal of Statistics and Management Systems 1. 22, 4(2019): 653-664.	2018	 
Stochastic voltage stability margin in unbalance feeder with fuzzy based distributed generation placement	J. P. Sharma and H. R. Kamath	International Journal of Engineering & Technology, Vol.7, No.2.21, pp 53-57, 2018.	2018	 
Influence of Solid State Fault Current Limiter on Grid Connected Photovoltaic System Protection	J.P. Sharma and H. R. Kamath	Journal of Clean Energy Technologies vol. 6, no. 3, pp. 254-257, 2018.	2018	 
Solving Wicked Problems: Searching for the Critical Cognitive Trait	Koushik Dutta	The International Journal of Management Education, 16(3), 493-503.	2018	 
Performance and Estimation of Culled Banking Stocks	Kirit Jainani and Rakhi Arora	International Journal of Management Studies 5(3), 55-62, July 2018.	2018	 
Availability improvement for the successive K-out-of-N machining system using standby with multiple working vacations	Sharma R. and Kumar G	International Journal of Reliability and Safety, Vol. 11, No. 3/4, pp. 256-267, 2017	2018	 
Housing Wealth Dis-saving Choices of Indian Urban Homeowners in Later Life: Influence of Uncertain Life Span and Demographics	Sarita Gupta and Sanjay Kumar	The IUP Journal of Applied Finance, 24 (4), 48-68	2018	 
2017
Title of paper	Name of the author/s	Name of journal	Year of publication	ISSN number
Make in India: A Sustainable Path to Management Education	Sheetal Mundra 	AIMS Journal of Management	2017	ISSN: 2395-6852
Indian Development: Regional Disparities on Selected Perspectives. International Journal of Trade & Global Business Perspectives	Sheetal Mundra and Lokanath Mishra 	Pezzottaite Journals, 6(2)	2017	 
A Conceptual Framework on Positive Leadership Style with Competency based Models	Richa Mishra and S. Jha 	International Journal on Leadership	2017	ISSN Number: 2321-1865
Performance of R 407 C as an alternative of R 22: A Review	S. Kasera and S. C. Bhaduri 	Energy Procedia, Elsevier	2017	ISSN: 1876-6102
Electrical, optical and electro photochemical studies on agarose based biopolymer electrolyte towards dye sensitized solar cell application	Rahul Singh, B. Bhattacharya, S.K. Tomar, Vijay Singh, Pramod K Singh 	Measurement	2017	ISSN: 0263-2241
Effect of crystal and   powder of CH3NH3I on the CH3NH3PbI3 based Perovskite sensitized solar cell	 Rahul, P.K. Singh, Rahul Singh, Vijay Singh, S. K. Tomar, B. Bhattacharya and Zishan H. Khan 	Material Research Bulletin 	2017	ISSN: 0025-5408
Statistical Analysis of Project Assessment Pattern of Examiners	Sunil Pathak, Umesh Gupta and Sonal Jain 	Research Outlook	2017	 
International Tourism Elasticity and Indian Economy	Rohit Dhanraj, Harshita Gupta, Umesh Gupta and Sheetal Mundra 	International Bulletin of Mathematical Research	2017	ISSN online 2394-7802
Finite Priority Queueing System with Service Interruption	Richa Sharma and Madhu Sharma 	International Journal of Industrial and Applied Mathematics	2017	 
Optimal N-policy for Unreliable Server Queue with Impatient Customer and Vacation interruption	 Richa Sharma 	Journal of Reliability and Statistical	2017	ISSN online 2229-5666 ISSN Print 0974- 8024
A Comparative Study of Facebook Marketing Practices of Selected Theme Based Restaurants in India	Ajay Chandel, Amit Sethi, and Punam Mishra 	Indian Journal of Marketing	2017	ISSN 09738703
Human Resource Disclosure and its Association with Corporate Attributes	Loknath Mishra and Richa Mishra	Global Journal of Management and Business Research: G Interdisciplinary	2017	ISSN: 0975-5853
Inter-linkages between human development and economic growth: a sustainable development analysis across Indian states	Sheetal Mundra and M. Singh 	International Journal of Indian Culture and Business Management	2017	ISSN online 1753-0814 ISSN print 1753-0806
Environmentally Concerned Consumer Behavior: Evidence from Consumers in Rajasthan	Pradeep Kautish and Ganesh Dash 	Journal of Modelling in Management	2017	ISSN: 1746-5664
Book Review:  “Strategic Marketing Management and Tactics in the Service Industry”	 Ganesh Dash 	International Journal of Information Systems in the Service Sector	2017	ISSN: 1935-5688
Vertical accuracy evaluation of SRTM-GL1, GDEM-V2, AW3D30 and CartoDEM-V3.1 of 30-m resolution with dual frequency GNSS for lower Tapi basin India	A O Jain, P Tejas Thaker, Ashish Chaurasia,  Thaker Tejas P, Chaurasia Ashish, Patel Parth, Singh Anupam K. 	Geocarto Int	2017	ISSN 10106049
Increasing light coupling in a photovoltaic film by tuning nanoparticle shape with substrate surface energy	Devika Kataria, K. Krishnamoorthy, S. Iyer and S. Kumar, S. 	Materials Research Express	2017	ISSN 2053-1591, P1753-0806
Role of Data mining in analyzing consumer’s online buying behavior	S. Taruna and Bhumika Pahwa 	International Journal of Business and Management Invention	2017	ISSN (Online)2319-8028  ISSN (Print) 2319-801X
Impact of photovoltaic distributed generation on unbalance phenomenon in distribution feeder	J. P. Sharma and H. R. Kamath 	Journal of Fundamental and Applied Sciences	2017	ISSN: 1112-9867
Investigation of dielectric properties of free standing electrospun nonwoven mat	Jitendra Tahalyani, Suwarna Datar and Balasubramanian Kandasubramanian 	Journal of Applied polymer science	2017	Print ISSN: 0021-8995 Online ISSN: 1097-4628
Dielectric and AC Conductivity Studies of Porous Armalcolite Nanocomposite based Novel Humidity Sensor	Ashis Tripathy, Sumit Pramanik, Ayan Manna, Zamri Radzi and Noor Azuan Abu
Osman 	Journal of the American Ceramic Society, Wiley Online Library	2017	Online ISSN:1551-2916
2016
Agarwal, H.P., (2016), “Voltage analysis of Tie-Line of Grid Solar System” published in the abstract volume of 4thRajasthan Science Congress at JK Lakshmipat University, Jaipur during 15-17 October 2016.
Bhaduri, S.C., and Kasera, S., (2016), “Solar Milk Refrigerator”, ASHRAE Bulletin, August 2016, Vol. 18, Issue 1
Dodiya, T., Jain, S., (2016), “Speech Recognition System for Medical Domain”, (IJCSIT) International Journal of Computer Science and Information Technologies, Vol. 7 (1) , 2016, 185-189,ISSN: 0975-9646
Dubey, A. K., Gupta, U.,  Jain, S., (2016), “Analysis of k-means clustering approach on the breast cancer Wisconsin dataset”, International Journal of Computer Assisted Radiology and Surgery, DOI 10.1007/s11548-016-1437-9, Print ISSN 1861-6410, Online ISSN 1861-6429, Springer Berlin Heidelberg
Kasera, S., Bhaduri, S.C., (2016), “Performance of R 407 C as an alternative of R 22: A Review”, RAAR 2016, Bhubaneshwar, Energy Procedia, Elsevier
Gupta, J., (2016), “Analysis and Estimation of Lomax-Weibull distribution”, Abstract published in Proceedings of 4th Rajasthan Science Congress on Leveraging Science and Technology for Resurgent Rajasthan, 15-17 October, 2016.
Gupta, U., Jain, S., (2016), “Impact of School Education on Performance in Higher Education (A Study on Engineering Students)”, International Journal of Technical Research & Science, ISSN NO : 2454-2024(Online), Vol 1, Issue 3
Jain, P., and Tyagi, V., (2016), “A survey of edge-preserving image denoising methods”, Information Systems Frontiers, vol. 18, no. 1, pp. 159-170, Springer Science, 2016. (SCIE Indexed, Impact Factor: 1.077).
Jain, S., Singhal, M., and Shah, A., (2016), “Exploring the Usage of Existing Plagiarism Tools for Automated Student Assessment for Java Program,” International Journal of Information and Education Technology vol. 6, no. 3, pp. 219-223, ISSN: 2010-3689.
Jain, S., (2016), “Enhanced Software Effort Estimation Using Multi Layered Feed Forward Artificial Neural Network Technique” at Twelfth International Conference on Communication Networks, ICCN 2016, August 19– 21, 2016, Bangalore, India
Kumar, P., Mathew, L., Shimi, S. L., Singh, P., (2016), “Advanced Power System configuration for sustainable grid” published in the proceedings of the International Conference on “Solar Energy & Smart grid: 2016” at KIIT University Bhubaneswar on 5-6 Feb. 2016.
Manglik, N., Jain, R., Singh, P. K., Bhattacharya, B., Singh, V., and Tomar, S. K., (2016), “Synthesis and properties of polyaniline, poly(o-anisidine), and poly[aniline-co-(o-anisidine)] using potassium iodate oxidizing agent”, High Performance Polymers (April 2016) DOI: 10.1177/0954008316639366
Poonia, G., and Sengar, S. S., (2016), “Distributed application of triangular array in SHF band”, 3rd international conference [IEEE Conference ID: 37465] on “computing for sustainable global development organized by BVICAM,New Dehli,16-18 march,2016.
Ranu, R., Chauhan, Y., Singh, P. K., Bhattacharya, B., and Tomar, S. K., (2016), “Electrical, structural and thermal studies of carbon nanotubes from natural legume seeds: kala chana”, Phase Transitions (February 2016), DOI: 10.1080/01411594.2016.1150473
Rijwani, P., Jain, S., (2016), Enhanced Software Effort Estimation Using Multi Layered Feed Forward Artificial Neural Network Technique, Procedia Computer Science, Elsevier Publishers, Volume 89, 2016, Pages 307–312, Twelfth International Conference on Communication Networks, ICCN 2016, August 19– 21, 2016, Bangalore, India
Sharma, J.P. and Kamath, H.R., (2016), “Fuzzy Logic Controller Based Distributed Generation Integration Strategy for Stochastic Performance Improvement”, Advances in Electrical Engineering, 2016.
Sharma, J. P., Chauhan, V., (2016),” Envisioning post domain of Restructured Accelerated Power Development and Reforms Programme-Fault current limiters”, National Conference on Solar ThermalEnergyTechnologies2016, IIT Jodhpur, 26 –28, February 2016.
Sharma, R. (2016). “Vacation Queue with Server Breakdown for MX/HK/1 Queue under N-Policy “, International Journal of Computer & Information Science, vol. 17, no. 1 (In Press).
Sharma R., Kaushik, M. and Kumar G., (2016),   “Reliability Analysis of an Embedded System with Multiple Vacations and Standby” published in the abstract volume of 4th Rajasthan Science Congress, “Leveraging Science and Technology for Resurgent Rajasthan” held during October 15-17, 2016 at JK Lakshmipat University, Jaipur, India.
Sharma, N. and Singh, K., (2016), “Quadratic Dynamic Matrix Control of Reactive Distillation Column for Synthesis of tert-Amyl Methyl Ether”, published in the abstract volume of 4th Rajasthan Science Congress “Leveraging Science and Technology for Resurgent Rajasthan” held during October 15-17, 2016 at JK Lakshmipat University, Jaipur, India.
Singh, R., Singh, P. K., Tomar, S. K., and Bhattacharya, B., (2016), “Synthesis, characterization and dye-sensitized solar cell fabrication using solid biopolymer electrolyte membranes”, High Performance Polymers, Vol. 28 (I) 47-54
2015
Arora, M., Sharma, A., and Ray, K., (2014). A ?- Slot Microstrip Antenna with Band Rejection Characteristics for Ultra Wideband Applications. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1135 – 1144.
Bhavsar, D., Sharma, J.P., (2014). Performance analysis of voice traffic over WiMAX using Qualnet Simulator, IEEE International Conference on Computational Intelligence and Computing Research, Dec. 18 – 20, 2014, ISBN No. 978-1-4799-3972-5/14/$31.00 ©2014 IEEE.
Bhavsar, D., Sharma, J.P., Bhagat, V., C., (2014). Research and challenges of swarm robotics, National Conference on Science and Engineering, July 27-28, 2014.
Dubey, A.K., Gupta, U., Jain, S., (2014) Breast Cancer Detection by Data Mining and Optimization: A Critical Survey, Third International Conference on Frontiers of Intelligent Computing: Theory and applications (FICTA ), Bhubaneswar, Orissa, 14-15 November 2014, Proceedings to be published by Springer.
Gupta, U., Hada, D.S., and Mathur, A., (2014). An Efficient Solution to Multiple Non-Linear Regression Model with Interaction Effect using TORA and LINDO. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 345 – 351.
Gupta, U., Jha, A. K. and Chaudhary, R. C. (2014), “Heat and Mass Transfer in MHD Three Dimensional Free Convective Flow Past a Vertical Surface with Periodic Suction”, International Bulletin of Mathematical Research, Vol. 1, No. 1, pp. 28-36, ISSN: 2394-7802
Hada, D. S., Sharma, S. C. and Gupta, U., (2014), “Seasonal Evaluation of Hydro-Geochemical Parameters using Goal Programming with Multiple Nonlinear Regression”, Gen. Math. Notes, Vol. 25, No. 2, pp. 137-147, ISSN 2219-7184
Jackisch, C., Zehe, E., Samaniego, L., and Singh, A. K. (2014). An Experiment to Gauge an Ungauged Catchment: Rapid Data Assessment and Eco-Hydrological Modelling in a Data Scarce Rural Catchment, Hydrological Sciences Journal, 59 (12), 2103-2125.
Jain, D., (2014). Birth of new Wireless Communication Technology: Light- Fidelity (Li-Fi), Proceedings of the 4th International Workshop on computer Science and Engineering (WCSE 2014) held in Dubai, UAE from   August 22-23, 2014. ?
Jain, N., Mathur, A., and Jain, D., (2014). Monitoring a water efficient Irrigation system through SCADA. Proceedings of the 3rd Naitonal Conference on Advances in Metrology (ADMET) – 2014 held at Thapar University, Patiala from February 19-21, 2014.
Jain, S., and Dodiya, T., (2014). Rule Based Architecture for Medical Question Answering System. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1225 – 1233.
Jain, S., Singhal, M., shah, A.,(2014). Exploring the Usage of Existing Plagiarism tools for Automated Student Assessment for Java Program, 6th International Conference on Computer Technology and Development (ICCTD 2014), 7-9 November, Hongkong,
Kaushik, M., and Kumar, G., (2014). Reliability Characterization for Embedded System with N- Version programming. Special issue of International Journal of Engineering and Technical Research, pp. 372-374.
Kedawat, G., Jain, V.K, and Vijay, Y. K., (2014). Fabrication of Metal Dielectric Metal Multilayer Thin Film: Color Filter. Proceeding of American Institute of Physics, 1591, 1024-1026.
Khanna, P., Jain, S., (2014). Distributed Cloud Federation Brokerage : A Live Analysis, International Journal of Science and Research, 3(12)
Khanna, P., Jain, S., Babu, B V, Distributed Cloud Brokerage: Solution to Real World Service Provisioning Problems, 2nd International Symposium on Big Data and Cloud Computing Challenges (ISBCC-15), Mar 2015, Kochi, India ( presented by Khanna, Prashant)
Khanna, P., Jain, S., (2014). Live Performance of Cloud Brokers in a Federation, International Journal of Science and Research Volume 3 Issue 12, December 2014 , ISSN (Online): 2319-7064
Khanna, P., Jain, S., Babu, BV, (2014). Cloud Broker: Working in federated structures, ICACCI, 3rd International Conference on Advances in Computing, Communications & Informatics, September 24-27, 2014, Delhi, India, pp.1273,1278, IEEE Explore, Print ISBN: 978-1-4799-3078-4, doi: 10.1109/ICACCI.2014.6968660
Lohat, S., and Kumar, S., Kaleidoscopic Shades of Indian Life in The God of Small Things, Q & A, and The White Tiger. Published in Online International Interdisciplinary Research Journal, ISSN2249-95098, Vol.IV, Sept.’14, pp. 207-216.
Naguri, J., Sharma, J.P., (2014). Review on indian power breakdown due to 400 KV Bina Gwalior Line Tripping, National Conference on Science and Engineering, July 27-28, 2014.
Pandey, A., Sharma, J.P., (2014). A Review on power generation by ultra-supercritical technology, National Conference on Science and Engineering, July 27-28, 2014.
Pathak, S., Dutta, N., and Jain, S., (2014). An Improved Cluster Maintenance Scheme for Mobile AdHoc Networks, ICACCI, 3rd International Conference on Advances in Computing, Communications & Informatics, September 24-27 , 2014, Delhi, India, pp.2117,2121, IEEE Explore, Print ISBN: 978-1-4799-3078-4, doi: 10.1109/ICACCI.2014.6968281
Phatak S. and Sharma R. (2014), A Comparative Analysis of Various Project Networking Techniques: A Review. International Journal of Engineering Research and Technology, vol. 3, no. 7, pp. 203-209.
Rijwani, P. and Jain, S.,(2014). Comparison and Analysis of Various Artificial Neural Networks for Software Effort Estimation Paper, International Journal of Advanced Research in Computer Science and Software Engineering (IJARCSSE), 4(12).
Rijwani, P., Jain, S., and Santani, D., (2014). Software Effort Estimation: A Comparison Based Perspective, International Journal of Application or Innovation in Engineering & Management (IJAIEM), Volume 3, Issue 12, ISSN 2319 – 4847
Sahoo, N., (2014). Multiple Model based Predictive Control of Magnetic Levitation System, 11th IEEE India conference INDICON2014, Pune, 11-13 December 2014.
Sharma, A. K., Mathur, V. and Jain, V. K., (2014). Fourier Transform Infrared Analysis of PS/PVC & PS/PMMA Polymeric Blends, Proceedings of National Conference on Science and Engineering (NCSE) at JK Lakshmipat University, Jaipur (Rajasthan) from July 27-28, 2014.
Sharma, J.P., Chauhan, V., Kamath, H.R., (2014). Modelling and Analysis of Solid State Fault Current Limiter, International Journal of Electrical, Electronics and Data Communication, 2(6).
Sharma, J.P., Chauhan, V., (2014). Application of Solid State Fault Current Limiter on Express Feeder for Voltage Sag Mitigation”, IEEE International Conference on Computational Intelligence and Computing Research, Dec. 18 – 20, 2014, ISBN No. 978-1-4799-3972-5/14/$31.00 ©2014 IEEE.
Sharma, J. P., and Kamath, H. R., (2014). Linear Hopfield Based Optimization for Combined Economic Emission Load Dispatch Problem. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 885 – 894.
Sharma, N. and Singh, K., (2014). Machine learning based control of Reactive Distillation Column, Proceedings of National Conference on Science and Engineering (NCSE) at JK Lakshmipat University, Jaipur (Rajasthan) from July 27-28, 2014.
Sharma, R., (2014). A Bulk Arrival Queue with Server Breakdown and Vacation under N- Policy. Proceeding of National Conference on Emerging Trends in Engineering & Technology held during March 30, 2014, at Abu, India.
Sharma, R. (2014). Mathematical Analysis of Queue with phases service: An overview, Advances in Operations Research, 2014, 1-19.
Sharma, R., and Kumar, G., (2014). Unreliable Server M/M/1 Queue with priority queueing system. Special issue of International Journal of Engineering and Technical Research, pp. 368-371.
Sharma, R. and Kumar G. (2014), Working Vacation Queue with K-phases Essential Service and Vacation Interruption. Souvenir of IEEE International Conference on Recent Advances and Innovations in Engineering held during May 09-11, 2014 at Poornima University Jaipur, India, 24.
Sharma, R. and Kumar G. (2014), Finite Priority M/M/1 Queue with Service Interruption. Souvenir of National Conference on Science and Engineering held during July 27-28, 2014 at J.K. Lakshmipat University Jaipur, India, pp. 33.
Sharma, S. B and Singh, A. K. (2014). Assessment of the Flood Potential on a Lower Tapi Basin Tributary using SCS-CN Method integrated with Remote Sensing & GIS data, Journal of Geography and Natural Disasters, 4:128. Doi: 10.4172/2167-0587.1000128.
Sharma, V., Sharma, J.P., (2014). Ladder Logic Algorithm for Automatic Vending Machine and Automatic Car Parking System, Journal of Basic and Applied Engineering Research, 1 (11), 70-73.
Singh, R., Pandey, S.P., Shukla, P.K., Tomar, S.K., Bhattacharya, B., and Singh, P.K., (2014). Synthesis of Lead Sulphide Nanoparticles for Electrode Application of Dye Sensitized Solar Cells. Nanoscience and Nanotechnology Letters, 6(1), 31-36.
.Tomar, S.K., Singh, R., Surana, K, Bhattacharya, B., and Singh, P. K., Growth,(2014) Statistical analysis of energy demand in photovoltaic system. Globalization & Governance: Promises and Challenges; 87-95, Proceeding of International conference on 3G 2014, ISBN: 978-93-83842-98-8
Toshniwal, S.K., and Ray, K., (2014). A Technique to Minimize the Effect on Resonance Frequency Due to Fabrication Errors of MS Antenna by Operating Dielectric Constant. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1145 – 1149.
Yadav, A., Tripathi, M.M., (2014). Modified Hysteresis Switching Scheme for 3 Phase Voltage Source Inverter, 6th IEEE POWER INDIA International Conference, 5-7 December 2014.
Yadav, A., Tripathi, M.M., (2014). A Novel Wavelet Modulation Scheme for Single Phase Inverter”, 6th IEEE POWER INDIA International Conference, 5-7 December 2014.
2014
Arora, M., Sharma, A., and Ray, K., (2014). A ?- Slot Microstrip Antenna with Band Rejection Characteristics for Ultra Wideband Applications. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1135 – 1144.
Bhavsar, D., Sharma, J.P., (2014). Performance analysis of voice traffic over WiMAX using Qualnet Simulator, IEEE International Conference on Computational Intelligence and Computing Research, Dec. 18 – 20, 2014, ISBN No. 978-1-4799-3972-5/14/$31.00 ©2014 IEEE.
Bhavsar, D., Sharma, J.P., Bhagat, V., C., (2014). Research and challenges of swarm robotics, National Conference on Science and Engineering, July 27-28, 2014.
Dubey, A.K., Gupta, U., Jain, S., (2014) Breast Cancer Detection by Data Mining and Optimization: A Critical Survey, Third International Conference on Frontiers of Intelligent Computing: Theory and applications (FICTA ), Bhubaneswar, Orissa, 14-15 November 2014, Proceedings to be published by Springer.
Gupta, U., Hada, D.S., and Mathur, A., (2014). An Efficient Solution to Multiple Non-Linear Regression Model with Interaction Effect using TORA and LINDO. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 345 – 351.
Gupta, U., Jha, A. K. and Chaudhary, R. C. (2014), “Heat and Mass Transfer in MHD Three Dimensional Free Convective Flow Past a Vertical Surface with Periodic Suction”, International Bulletin of Mathematical Research, Vol. 1, No. 1, pp. 28-36, ISSN: 2394-7802
Hada, D. S., Sharma, S. C. and Gupta, U., (2014), “Seasonal Evaluation of Hydro-Geochemical Parameters using Goal Programming with Multiple Nonlinear Regression”, Gen. Math. Notes, Vol. 25, No. 2, pp. 137-147, ISSN 2219-7184
Jackisch, C., Zehe, E., Samaniego, L., and Singh, A. K. (2014). An Experiment to Gauge an Ungauged Catchment: Rapid Data Assessment and Eco-Hydrological Modelling in a Data Scarce Rural Catchment, Hydrological Sciences Journal, 59 (12), 2103-2125.
Jain, D., (2014). Birth of new Wireless Communication Technology: Light- Fidelity (Li-Fi), Proceedings of the 4th International Workshop on computer Science and Engineering (WCSE 2014) held in Dubai, UAE from   August 22-23, 2014. ?
Jain, N., Mathur, A., and Jain, D., (2014). Monitoring a water efficient Irrigation system through SCADA. Proceedings of the 3rd Naitonal Conference on Advances in Metrology (ADMET) – 2014 held at Thapar University, Patiala from February 19-21, 2014.
Jain, S., and Dodiya, T., (2014). Rule Based Architecture for Medical Question Answering System. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1225 – 1233.
Jain, S., Singhal, M., shah, A.,(2014). Exploring the Usage of Existing Plagiarism tools for Automated Student Assessment for Java Program, 6th International Conference on Computer Technology and Development (ICCTD 2014), 7-9 November, Hongkong,
Kaushik, M., and Kumar, G., (2014). Reliability Characterization for Embedded System with N- Version programming. Special issue of International Journal of Engineering and Technical Research, pp. 372-374.
Kedawat, G., Jain, V.K, and Vijay, Y. K., (2014). Fabrication of Metal Dielectric Metal Multilayer Thin Film: Color Filter. Proceeding of American Institute of Physics, 1591, 1024-1026.
Khanna, P., Jain, S., (2014). Distributed Cloud Federation Brokerage : A Live Analysis, International Journal of Science and Research, 3(12)
Khanna, P., Jain, S., Babu, B V, Distributed Cloud Brokerage: Solution to Real World Service Provisioning Problems, 2nd International Symposium on Big Data and Cloud Computing Challenges (ISBCC-15), Mar 2015, Kochi, India ( presented by Khanna, Prashant)
Khanna, P., Jain, S., (2014). Live Performance of Cloud Brokers in a Federation, International Journal of Science and Research Volume 3 Issue 12, December 2014 , ISSN (Online): 2319-7064
Khanna, P., Jain, S., Babu, BV, (2014). Cloud Broker: Working in federated structures, ICACCI, 3rd International Conference on Advances in Computing, Communications & Informatics, September 24-27, 2014, Delhi, India, pp.1273,1278, IEEE Explore, Print ISBN: 978-1-4799-3078-4, doi: 10.1109/ICACCI.2014.6968660
Lohat, S., and Kumar, S., Kaleidoscopic Shades of Indian Life in The God of Small Things, Q & A, and The White Tiger. Published in Online International Interdisciplinary Research Journal, ISSN2249-95098, Vol.IV, Sept.’14, pp. 207-216.
Naguri, J., Sharma, J.P., (2014). Review on indian power breakdown due to 400 KV Bina Gwalior Line Tripping, National Conference on Science and Engineering, July 27-28, 2014.
Pandey, A., Sharma, J.P., (2014). A Review on power generation by ultra-supercritical technology, National Conference on Science and Engineering, July 27-28, 2014.
Pathak, S., Dutta, N., and Jain, S., (2014). An Improved Cluster Maintenance Scheme for Mobile AdHoc Networks, ICACCI, 3rd International Conference on Advances in Computing, Communications & Informatics, September 24-27 , 2014, Delhi, India, pp.2117,2121, IEEE Explore, Print ISBN: 978-1-4799-3078-4, doi: 10.1109/ICACCI.2014.6968281
Phatak S. and Sharma R. (2014), A Comparative Analysis of Various Project Networking Techniques: A Review. International Journal of Engineering Research and Technology, vol. 3, no. 7, pp. 203-209.
Rijwani, P. and Jain, S.,(2014). Comparison and Analysis of Various Artificial Neural Networks for Software Effort Estimation Paper, International Journal of Advanced Research in Computer Science and Software Engineering (IJARCSSE), 4(12).
Rijwani, P., Jain, S., and Santani, D., (2014). Software Effort Estimation: A Comparison Based Perspective, International Journal of Application or Innovation in Engineering & Management (IJAIEM), Volume 3, Issue 12, ISSN 2319 – 4847
Sahoo, N., (2014). Multiple Model based Predictive Control of Magnetic Levitation System, 11th IEEE India conference INDICON2014, Pune, 11-13 December 2014.
Sharma, A. K., Mathur, V. and Jain, V. K., (2014). Fourier Transform Infrared Analysis of PS/PVC & PS/PMMA Polymeric Blends, Proceedings of National Conference on Science and Engineering (NCSE) at JK Lakshmipat University, Jaipur (Rajasthan) from July 27-28, 2014.
Sharma, J.P., Chauhan, V., Kamath, H.R., (2014). Modelling and Analysis of Solid State Fault Current Limiter, International Journal of Electrical, Electronics and Data Communication, 2(6).
Sharma, J.P., Chauhan, V., (2014). Application of Solid State Fault Current Limiter on Express Feeder for Voltage Sag Mitigation”, IEEE International Conference on Computational Intelligence and Computing Research, Dec. 18 – 20, 2014, ISBN No. 978-1-4799-3972-5/14/$31.00 ©2014 IEEE.
Sharma, J. P., and Kamath, H. R., (2014). Linear Hopfield Based Optimization for Combined Economic Emission Load Dispatch Problem. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 885 – 894.
Sharma, N. and Singh, K., (2014). Machine learning based control of Reactive Distillation Column, Proceedings of National Conference on Science and Engineering (NCSE) at JK Lakshmipat University, Jaipur (Rajasthan) from July 27-28, 2014.
Sharma, R., (2014). A Bulk Arrival Queue with Server Breakdown and Vacation under N- Policy. Proceeding of National Conference on Emerging Trends in Engineering & Technology held during March 30, 2014, at Abu, India.
Sharma, R. (2014). Mathematical Analysis of Queue with phases service: An overview, Advances in Operations Research, 2014, 1-19.
Sharma, R., and Kumar, G., (2014). Unreliable Server M/M/1 Queue with priority queueing system. Special issue of International Journal of Engineering and Technical Research, pp. 368-371.
Sharma, R. and Kumar G. (2014), Working Vacation Queue with K-phases Essential Service and Vacation Interruption. Souvenir of IEEE International Conference on Recent Advances and Innovations in Engineering held during May 09-11, 2014 at Poornima University Jaipur, India, 24.
Sharma, R. and Kumar G. (2014), Finite Priority M/M/1 Queue with Service Interruption. Souvenir of National Conference on Science and Engineering held during July 27-28, 2014 at J.K. Lakshmipat University Jaipur, India, pp. 33.
Sharma, S. B and Singh, A. K. (2014). Assessment of the Flood Potential on a Lower Tapi Basin Tributary using SCS-CN Method integrated with Remote Sensing & GIS data, Journal of Geography and Natural Disasters, 4:128. Doi: 10.4172/2167-0587.1000128.
Sharma, V., Sharma, J.P., (2014). Ladder Logic Algorithm for Automatic Vending Machine and Automatic Car Parking System, Journal of Basic and Applied Engineering Research, 1 (11), 70-73.
Singh, R., Pandey, S.P., Shukla, P.K., Tomar, S.K., Bhattacharya, B., and Singh, P.K., (2014). Synthesis of Lead Sulphide Nanoparticles for Electrode Application of Dye Sensitized Solar Cells. Nanoscience and Nanotechnology Letters, 6(1), 31-36.
.Tomar, S.K., Singh, R., Surana, K, Bhattacharya, B., and Singh, P. K., Growth,(2014) Statistical analysis of energy demand in photovoltaic system. Globalization & Governance: Promises and Challenges; 87-95, Proceeding of International conference on 3G 2014, ISBN: 978-93-83842-98-8
Toshniwal, S.K., and Ray, K., (2014). A Technique to Minimize the Effect on Resonance Frequency Due to Fabrication Errors of MS Antenna by Operating Dielectric Constant. B. V. Babu et al. (eds.), Proceedings of the Second International Conference on Soft Computing for Problem Solving (SocProS 2012), December 28–30, 2012, Advances in Intelligent Systems and Computing, 236, 1145 – 1149.
Yadav, A., Tripathi, M.M., (2014). Modified Hysteresis Switching Scheme for 3 Phase Voltage Source Inverter, 6th IEEE POWER INDIA International Conference, 5-7 December 2014.
Yadav, A., Tripathi, M.M., (2014). A Novel Wavelet Modulation Scheme for Single Phase Inverter”, 6th IEEE POWER INDIA International Conference, 5-7 December 2014.
2013
Bhavsar, D., and Badnakhe, M., (2013). E-learning Paradigm for Teaching Enhancements. In Ford Lumban Gaol, Benfno Soewito, Mohamed Bououdina and Mu-Song Chen (Eds.), Proceedings of the 2013 International Conference on Computer Graphics, Visualization, Computer Vision, and Game Technology, Advances in Intelligent Systems Research Journal, 53, 20-25.
Jain, M., Sharma, R., and Sharma, G.C., (2013). Multiple vacation policy for MX/Hk/1 queue with un-reliable server. Journal of Industrial Engineering International: A Springer Open Journal, 9(36), 1-11.
Jain, S., and Pareek, J., (2013). Automatic Extraction of Prerequisites and Learning Outcome from Learning Material. International Journal of Metadata, Semantics and Ontologies 8.2, Special Issue on New Challenges in Resource Discovery, 145-154.
Jain, V.K., Kedawat, G., Agrawal, S., Vijay, Y.K., (2013). Annealing Influence on Optical Properties of IZO Thin Films. International Journal of Recent Research and Review, 5, 7-9.
Kaushik, M., and Kumar, G., (2013). Software Reliability of Embedded Computer Systems: An Overview. In the Electronic Proceeding of 8th Biyani International Conference on Amplification of Futuristic Technology by an Integrated Approach of Computing, Engineering and System Science held at Jaipur from September 22-26, 131-135.
Kedawat, G., Jain, V.K., Srivastava, S., and Vijay, Y.K., (2013). A Novel High Transmittance Red Colour Filter:ZnS and Ag Multilayer. In the Proceeding of American Institute of Physics, 1512, 760-761.
Kedawat, G., Srivastava, S., Jain, V.K., Kumar, P., Kataria, V., Agrawal, Y., Gupta, B.K., and Vijay, Y.K., (2013). Fabrication of Artificially Stacked Ultrathin ZnS/MgF2 Multilayer Dielectric Optical Filters, ACS Applied Materials & Interfaces, 5(11), 4872–4877.
Kumar, S., (2013). Linguistic Improvisations in Indian English: A Cultural Perspective. In Pushp Lata, Devika and G.S.Chauhan (Eds.), Integrating Web 2.0 Technology and Culture in ELT: Post-Conference Proceedings of Third ELT@I Rajasthan International Conference on Interfacing Language, Culture, and Technology. New Delhi: Jain Brothers, 251-266.
Kumar, S., (2013). Culture Re-contextualized: A Comparative Study of Jhumpa’s ‘The Namesake’ and Jaishree’s ‘The Ancient Promises’. The American International Journal of Research in Humanities, Arts and Social Sciences, March-May, 1(2), 1-9.
Lata, P., Kumar, S., Dey, A., and Chakraborty,O., (2012). Revisiting R.K.Narayan’s The Guide on Silver Screen. The Southeast Asian Journal of English Language Studies, 18 (1), 1-10.
Pathak, S., and Jain, S., (2013). A Survey: On Unicast Routing Protocols for Mobile Ad Hoc Network. International Journal of Emerging Technology & Advanced Engineering, 3(1).
2012
Agarwal, R., and Parihar, H.S., (2012). On Certain Generalized Polynomial System Associated with Humbert Polynomials. Scientia Series A: Mathematical Sciences, 23, 31-44.
Babu, B.V., Sharma, R., and Sheth, P.N., (2012). Kinetic Modeling & Simulation of Thermo-Chemical Conversion of Jatropha de-oiled Cake. In the Proceedings of 2012 AIChE Annual Meeting on ‘Cleaner Energy, Stronger Economy, Better Living’ at Pittsburgh, PA, USA from October 28 – November 02.
Bhattacharya, B., Tomar, S.K., Pandey, S.P., Rhee, H.W., and Singh, P.K., (2012). Porous Nanocrystalline TiO2 Electrode and Poly (N-methyl 4-vinylpyridine iodide) – Ionic Liquid Solid Polymer Electrolyte for Device Application. International Journal of Nanotechnology, 9 (10/11/12), 1030-1039.
Datta, D., Kumar, S., Wasewar, K.L., and Babu, B.V., (2012). Comparative Study on Reactive Extraction of Picolinic Acid with Six Different Extractants (Phosphoric and Aminic) in Two Different Diluents (Benzene and Decane-1-ol). Separation Science and Technology, 47, 997-1005.
Dodiya, T., and Jain, S., (2012). Comparison of Question Answering Systems, Intelligent Informatics. Series Title: Advances in Intelligent Systems and Computing, Proceedings of the International Symposium on Intelligent Informatics ISI’12 held at Chennai, India. Heidelberg, Berlin, Germany: Springer, 182, 99-107
Gujarathi, A.M., and Babu, B.V., (2012). Differential Evolution Strategies for Multiobjective Optimization. In the Kusum Deep, Atulya Nagar, Millie Pant and Jagdish Chand Bansal (Eds.), Proceedings (Vol. 1) of the International Conference on Soft Computing for Problem Solving (SocProS 2011) held at IIT Roorkee from December 20-22. Springer Series: Advances in Intelligent and Soft Computing (AISC), 130, 63–72.
Gupta, N., Kumar, D., and Tomar, S.K., (2012). Thermal Behaviour of Chemically Synthesized Polyanilines/Polystyrene Sulphonic Acid Composites. International Journal of Materials and Chemistry, 2(2), 79-85.
Jain, A., and Babu, B.V., (2012). Analysis of Process Interactions in Dynamic Systems Using Frequency Dependent RGA. Advanced Materials Research, 403-408, 895-899.
Jain, V.K., Kumar, P., Srivastava, S., and Vijay, Y.K., (2012). Fabrication of Zinc Indium Oxide Thin Films and Effect of Post Annealing on Structural, Chemical and Electrical Properties. Journal of Alloys and Compound 530, 132-137
Jain, V.K., Kumar, P., and Vijay, Y.K., (2012). Preparation of Nanostructure ZnO-SnO2 Thin Films for Optoelectronic Properties and Post Annealing Influence. World Academy of Science, Engineering and Technology, 72, 1728-1730.
Khan, M.S., and Naqvi, A., (2012). Synthesis and Molecular Docking Studies of N-(4-Bromo-2 fluorophenyl) Malonamide. Research Journal of Pharmaceutical, Biological and Chemical Sciences, 3 (4), 49-52.
Kumar, S., (2012). Revisiting R. K. Narayan’s The Guide on Silver Screen.” Published in 3L: Language, Linguistics, Literature – The Southeast Asian Journal of English Language Studies, 18(1), 1-10.
Kumar, S., Datta, D., and Babu, B.V., (2012). Reactive Extraction of Nicotinic Acid using Tri-n-Octylphosphine Oxide (TOPO) Dissolved in a Binary Diluent Mixture. In the Proceedings of 2012 AIChE Annual Meeting on ‘Cleaner Energy, Stronger Economy, Better Living’ at Pittsburgh, PA, USA from October 28 – November 02.
Phogat, K.S., Sharma, A.K., Ranjan, R.K., and Bajpai, V.K., (2012). An Upper Bound Solution for Forging Load of an Elliptical Disc. Journal of Mechanical Engineering Research, 4 (4), 130-135.
Raghuvanshi, S., Gupta, S., and Babu, B.V., (2012). Application of Biofilter System for Removal of Ethyl Acetate: Kinetic and Column Studies. In the Proceedings of 2012 AIChE Annual Meeting on ‘Cleaner Energy, Stronger Economy, Better Living’ at Pittsburgh, PA, USA from October 28 – November 02.
Ray, K., (2012). Thomas-Fermi Calculation in Constituent Quark Nucleon Nucleon Interaction and Nuclear Matter. International Journal of Advances in Engineering, Science and Technology, 1 (2), 273.
Ray, K., (2012). An Electromagnetic-Neurophysiological Model of Memory. The International Journal of Electromagnetics and Applications, 2 (1), 1-3.
Ray, K., (2012). Effect of External Oscillating Field on Biological Systems. International Journal of Advances in Engineering, Science and Technology, 2 (1), 327.
Ray, K., (2012). Exploring the Possibility of treating Müller Cells as Nano Horn Antennas. International Journal of Advances in Engineering, Science and Technology, 1 (2), 276.
Shah, A., Jain, S., Chheda, R., and Mashru, A., (2012). Model for Reranking Agent on Hybrid search engine for E-Learning. In the Proceedings of IEEE Fourth International Conference on Technology for Education, IEEE Explore, 247-248.
2011
Agrawal, S., Tripathi, B., Kumar, S., Jain, V.K., Srivastava, S., and Vijay, Y.K., (2011). Ni+7 Ion Beam Effect on Ag Doped ZnS Nanocrystals Embeded in PMMA Matrix. In the Proceeding of American Institute of Physics, 1349, 387-388.
Gujarathi, A.M., and Babu, B.V., (2011). Hybrid Multi-objective Differential Evolution for Multi-objective Optimization of Industrial Polymeric Materials. In the Proceedings of XXVIII Conference on Computer Methods in Materials Technology (KomPlastTech-2011) held at Zakopane, Poland from January 16-19. Computer Methods in Material Science, 11 (3), 463-468.
Gujarathi, A.M., and Babu, B.V., (2011). Multi-objective Optimization of Industrial Processes using Elitist Multi-objective Differential Evolution (Elitist- MODE). Materials and Manufacturing Processes, 26(3), 455-463.
Gujarathi, A.M., Motagamwala, A.H., and Babu, B.V., (2011). Multi-objective Differential Evolution with Improved Selection Scheme (MODE III-ISS) for Optimization of Industrial Naphtha Cracker Unit. In the Proceedings of IEEE Symposium Series on ‘Computational Intelligence’ (SSCI’2011): Symposium on Differential Evolution (SDE-2011) held at Paris, France from April 11-15.
Gupta, U., Jha, A.K., and Chaudhary, R.C., (2011). Free Convection Flow between Vertical Plates Moving in Opposite Direction and Partially Filled with Porous Medium. Applied Mathematics, 2, 935-941
Jain, A., and Babu, B.V., (2011). Relative Gain Array Analysis for Process Model Uncertainty: A Worst-case Bound. In the Proceedings of International Conference on ‘Science & Engineering’ (ICSE-2011), held at HUDA, Rohtak from January 21 -23.
Jain, A., and Babu, B.V., (2011). Analyzing Effective Relative Energy Array (EREA) as a Criterion for Input–Output Pairing of Multivariable Processes. In the Proceedings of 19th IEEE Workshop on ‘Nonlinear Dynamics of Electronic Systems (NDES-2011)’ held at Kolkata from March 9-11.
Jain, A., and Babu, B.V., (2011). Analysis of Process Interactions in Dynamic Systems Using Frequency Dependent RGA. In the Proceedings of International Conference on ‘Control, Robotics and Cybernetics’ (ICCRC-2011) held at New Delhi from March 19-20.
Jain, A., and Babu, B.V., (2011). A Comparitive Study on Input–Output Pairing of Dynamic Process Systems. In the Proceedings of Second International Conference on ‘Advances in Power Electronics and Instrumentation Engineering’ (PEIE-2011) held at Nagpur from April 21 – 22. Also published in Journal of Engineering Research and Studies, II (III), 137-141.
Jain, A., Singh, D., and Babu, B.V. (2011). Analyzing Input-Output Pairing of Uncertain Multivariable Plants using Relative Gain Array: A Graphical Approach. In the Proceedings of International Symposium & 64th Annual Session of IIChE in association with International Partners (CHEMCON -2011) held at Bangalore from December 27-29.
Jain, L., and Mahor, D., (2011). Application of Hough Transform for Finding Parametric Curves. International Journal of Computer Applications in Engineering Sciences, 1(2), 100-103.
Jain, V.K., Kumar, P., Bhandari, D., and Vijay, Y.K., (2011). Effect of Annealing and SnO2 Addition on Properties of Nano-Structured Zno Thin Films. International Journal of Nanoscience, 4, 1-5.
Jain, V.K., Kumar, P., Jain, P., Srivastava, S., and Vijay, Y.K., (2011). Growth and Annealing influence on Structural and Optical Properties of Nanostructured ZIO Thin Films. In the Proceeding of American Institute of Physics, 1349, 635-636.
Jain, V.K., Kumar, P., Kumar, M., Jain, P., Bhandari, D., and Vijay, Y.K., (2011). Study of Post Annealing Influence on Structural, Chemical and Electrical Properties of ZTO Thin Films. Journal of Alloys and Compound, 509, 3541-3546.
Khanna, P., and Babu, B.V., (2011). Cloud Computing Brokering Service: A Trust Framework – Service Level Agreements: An Analytical Study in Progress. In the Proceedings of CLOUD COMPUTING 2012: The Third International Conference on ‘Cloud Computing, GRIDs, and Virtualization’ held at Nice, France from July 22-27.
Kumar, S., and Babu, B.V., (2011). Equilibrium and Kinetic Studies on Reactive Extraction of Propionic Acid using Tri-n-Octylamine (TOA) Dissolved in Cyclohexane+1Decanol (1:1v/v). In the Proceedings of 2011 Annual Meeting of AIChE held at Minneapolis, MN, USA from October 16-21.
Kumar, S., Datta, D., and Babu, B.V., (2011). Estimation of Equilibrium Parameters using Differential Evolution in Reactive Extraction of Propionic Acid by Tri-n-Butyl Phosphate. Chemical Engineering and Processing: Process Intensification, 50 (7), 614-622.
Kumar, S., Datta, D., and Babu, B.V., (2011). Differential Evolution Approach for Reactive Extraction of Propionic Acid using Tri-n-Butyl Phosphate (TBP) in Kerosene and 1-Decanol. Materials and Manufacturing Processes, 26 (9), 1222-1228.
Raghuvanshi, S., Gupta, S., and Babu, B.V., (2011). Application of Biofilter System for Removal of Ethyl Acetate. In the Proceedings of International Symposium & 64th Annual Session of IIChE in association with International Partners (CHEMCON-2011) held at Bangalore from December 27-29.
Ray, K., (2011). Analysis of Minimal Distortion Loss during Image Transfer Using M?ller Cells Treated as Horn Antennas. In the Proceeding of the First National Conference on ‘Applied Mathematical Sciences’ held at Sikkim, 27-32.
Ray, K., (2011). Memory: A Brain Wave Approach. Proceeding of the 10th biennial International Conference on ‘Vibration Problems’ (ICoVP-2011) held at PRAGUE, Czech Republic, 467-471
Srivastava, S., Kumar, S., Jain, V.K., and Vijay, Y.K., (2011). Effect of Temperature on the Electrical and Gas Sensing Properties of Polyaniline and Multiwall Carbon Nanotube Doped Polyaniline Composite Thin Films. Advanced Materials Research, 254, 167-170.

"""

def format_data(text):
    # Regex for tabular data (e.g., research paper entries)
    tabular_pattern = re.compile(r'(.*?)\s{4,}(.*?)\s{4,}(.*?)\s{4,}(.*?)\s{4,}(.*?)$', re.MULTILINE)
    
    formatted_output = ""
    current_year = None
    in_table = False  # Flag to track if we are in the table section

    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        # Detect year headers
        if line.isdigit():
            current_year = line
            formatted_output += f"\n### Research Papers {current_year}\n\n"
            in_table = True
            continue
        
        # Process tabular data (Research papers)
        if in_table:
            match = tabular_pattern.match(line)
            if match:
                title, authors, journal, year, issn = match.groups()
                formatted_output += (
                    f"- **Title**: {title.strip()}\n"
                    f"  **Authors**: {authors.strip()}\n"
                    f"  **Journal**: {journal.strip()}\n"
                    f"  **Year**: {year.strip()}\n"
                    f"  **ISSN**: {issn.strip()}\n\n"
                )
            else:
                # Exit table mode if no match found
                in_table = False
        
        # Process non-tabular (narrative) sentences
        if not in_table:
            formatted_output += line + "\n\n"
    
    return formatted_output

# Call the function and print the result
formatted_text = format_data(input_text)
print(formatted_text)

# Optional: Save the formatted text to a file
with open('formatted_data.txt', 'w') as file:
    file.write(formatted_text)
