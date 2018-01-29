Title: My favorite scientific papers of 2017
Date: 2018-01-27 17:00
Category: Research


Last year I set a goal to write something each month on the blog. Obviously, I failed. However, I want to share my yearly list of the best scientific paper I read during the previous twelve months. Here is [the list for 2016](http://www.marcodena.it/blog/my-favorite-scientific-papers-of-2016/), and 2017 follows:


1. [Connective recovery in social networks after the death of a friend](https://www.nature.com/articles/s41562-017-0092)[^1]. What's the resilience of social networks after a death? Do individuals communicate more with friends who did not know the person who died? Do people try to create new interactions to "compensate" the friend? How is the number of interactions dependent on age and cause of death? This is the classic paper that only Facebook can write. A masterpiece just because is the first time we can track this kind of information from a large number of people. I hope to see future similar works, controlling for culture co-variates as well. ![ego network death facebook](/images/ego-network-death-facebook.png)

2. [Human Perception of Performance](https://arxiv.org/abs/1712.02224)[^2]. Very beautiful analysis of human evaluation in a sport. With a framework called observe-predict-explain they analyze football data through objective metrics and subjective evaluations of sports experts, then they predict the performance and explain factors that influence it. This paper suggests that contextual information influence evaluations of performance and that human judge performance on a limited number of heuristics.

3. [Luck is Hard to Beat: The Difficulty of Sports Prediction](https://dl.acm.org/citation.cfm?id=3098045)[^3]. "Sports outcomes is a mix of skills and good and bad luck. This mix is responsible for large part of the sports appeal". The paper starts with these phrases and creates a Bayesian model that fits the data of four different sports (basketball, soccer, volleyball, and handball) to explore the role of luck and skills in the outcome of games. Elegant idea, very well written. 

4. [Computer vision uncovers predictors of physical urban change](http://www.pnas.org/content/114/29/7571.short)[^4]. Nikil and Hidalgo succeed again with a new paper linking the improvement of places with various urban theories. Are changes of physical appearance connected with socio-economical characteristics of people (e.g., education)? Is there a spillover effect on the improvement-decay of neighborhoods? This paper shows how computer vision techniques can now be applied to explore urban characteristics over time. ![Hidalgo street change](/images/streetchange.jpg)

5. [POI2Vec: Geographical Latent Representation for Predicting Future Visitors](https://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14902)[^5]. My journey on future locations prediction with Deep Learning started here. This paper tries to predict future visitors of POIs, from the perspective of the place (not of the user). However, differently from other [putsomethinghere]2vec papers, POI2Vec creates a latent representation of the geographical context, looking at POIs that are nearby. Very interesting formulation of KD-trees in a "deep learning way."

6. [Prediction and explanation in social systems](http://science.sciencemag.org/content/355/6324/486)[^6]. A must-read paper for all data-scientists working on computational social science. Metrics, predictions and best practices explained very well.

7. [Computational social scientist beware: Simpson’s paradox in behavioral data](https://link.springer.com/article/10.1007/s42001-017-0007-4)[^7]. A paper explaining all the pitfalls of heterogeneous data, which can generate aggregated results that are different from those of the underlying subgroups. The author also describes some mechanisms to control for possible problems in the datasets.

8. [Can cascades be predicted?](https://dl.acm.org/citation.cfm?id=2567997)[^8]. Yes! I mean, first we have to define prediction. This paper defines prediction of cascades answering the question "will the cascade of size k reach 2k?". In other words, can our Facebook post reach virality? Does virality depend on users/pages/type of content? If you work with social-network data, please read this paper.

9. [Evidence that curtailing proactive policing can reduce major crime](https://www.nature.com/articles/s41562-017-0211-5)[^9]. A causal model that shows how low-level arrests reduce serious crime. Supported by data, and well written.

10. [Using Convolutional Networks and Satellite Imagery to Identify Patterns in Urban Environments at a Large Scale](https://dl.acm.org/citation.cfm?id=3098070)[^10]. A very well written paper that uses standard Convolutional Neural Network and open data to predict land use in various cities in the world. Can we learn from one city and predict in another? How can we analyze land-use patterns automatically in different cities? A VERY well written paper with [documented code and Jupyter notebooks](https://github.com/adrianalbert/urban-environments) as well!

<iframe width="637" height="315" src="https://www.youtube.com/embed/MPttLQVU_wY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


Thanks!





[^1]: Hobbs, William R., and Moira K. Burke. "Connective recovery in social networks after the death of a friend." Nature Human Behaviour 1.5 (2017): 0092.
[^2]: Pappalardo, Luca, et al. "Human Perception of Performance." arXiv preprint arXiv:1712.02224 (2017).
[^3]: Aoki, Raquel, Renato M. Assuncao, and Pedro OS Vaz de Melo. "Luck is hard to beat: The difficulty of sports prediction." Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 2017.
[^4]: Naik, Nikhil, et al. "Computer vision uncovers predictors of physical urban change." Proceedings of the National Academy of Sciences 114.29 (2017): 7571-7576.
[^5]: Feng, Shanshan, et al. "POI2Vec: Geographical Latent Representation for Predicting Future Visitors." AAAI. 2017.
[^6]: Hofman, Jake M., Amit Sharma, and Duncan J. Watts. "Prediction and explanation in social systems." Science 355.6324 (2017): 486-488.
[^7]: Lerman, Kristina. "Computational social scientist beware: Simpson’s paradox in behavioral data." Journal of Computational Social Science (2017): 1-10.
[^8]: Cheng, Justin, et al. "Can cascades be predicted?." Proceedings of the 23rd international conference on World wide web. ACM, 2014.
[^9]: Sullivan, Christopher M., and Zachary P. O’Keeffe. "Evidence that curtailing proactive policing can reduce major crime." Nature Human Behaviour 1.10 (2017): 730.
[^10]: Albert, Adrian, Jasleen Kaur, and Marta C. Gonzalez. "Using convolutional networks and satellite imagery to identify patterns in urban environments at a large scale." Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 2017.


