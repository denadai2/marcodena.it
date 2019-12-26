Title: My favorite scientific papers of 2019
Date: 2019-12-26 16:00
Category: Research

2019 is almost ended, so it is time to wrap-up the annual list of the best scientific papers of the year.
It is the fourth time I write this feature, and I really enjoy going through my lists of [2018](https://www.marcodena.it/blog/my-favorite-scientific-papers-of-2018/), [2017](https://www.marcodena.it/blog/my-favorite-scientific-papers-of-2017/) and [2016](https://www.marcodena.it/blog/my-favorite-scientific-papers-of-2016/). 
However, I am not alone in doing this. 
Nicola Perra listed [the top 10 articles](http://www.nicolaperra.com/twitter-top-10-2019.html) for the number of engagements from the [NetScience twitter profile](https://twitter.com/net_science), while the community of 'r/MachineLearning' listed the [best paper of 2019 for the Machine Learning community](https://www.reddit.com/r/MachineLearning/comments/e8the3/d_what_was_your_favorite_paper_of_2019_and_why/).


1. [Tackling Climate Change with Machine Learning](https://arxiv.org/abs/1906.05433)[^1]. Thanks (mainly) to Greta Thunberg, mass media amply discussed climate change. 
The research community was no exception. Many have focused on the increasing cost of Deep Learning models, while others have concentrated on their potentialities. 
Specifically, 21 researchers wrote an article that collects recent trends and discoveries that might help alleviating climate change. 
These discoveries are organized by field (e.g. Industry, Buildings and cities) and strategies (e.g. long-term, uncertain impact). 
As a bonus, I also suggest [GreenAI](https://arxiv.org/abs/1907.10597)[^2], which explains the complexity and efficiency of recent Deep Learning models. I think that, by increasing awareness on the environmental cost of our models, we might think twice about the trade-off between complexity and models' performance.
<iframe width="560" height="315" src="https://www.youtube.com/embed/O2VyykXbDc4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

2. [Modelling opinion dynamics in the age of algorithmic personalization](https://www.nature.com/articles/s41598-019-43830-2)[^3]. Modern technology has greatly influenced how we access information, form opinions and interact with other people. 
We have access to an increasing amount of information, which is easily accessible through or devices, and we are able to communicate with other people without being affected by geographical constraints. However, our attention is affected by cognitive constraints.
Algorithms such as those that control the Facebook and Instagram timelines can distil information for us. How do they shape our opinions’ share and distributions? How do filtering algorithms influence people's polarization?
This paper develops a mechanistic model to explain exactly this. 

3. [Sha-RNN](http://science.sciencemag.org/content/359/6373/325)[^4]. Not only is this paper useful, but also funny to read!  
It discusses a new Deep Learning module, called SHA-RNN, that allows to model long-term dependencies of data with fewer parameters and without LSTMs.
Even if you do not work in the NLP field, it might be useful to read it!
    ![sha-rnn-paper](/images/SHA-RNN.png)
   
4. [Auto-encoding variational bayes](https://arxiv.org/abs/1312.6114)[^5]. I reached this paper pretty late, but it is a masterpiece of Machine Learning. Variational Auto-Encoders (VAEs) greatly influenced my research as they allow to stochastically sampling from a learned distribution.

5. [SpotTune: transfer learning through adaptive fine-tuning](http://openaccess.thecvf.com/content_CVPR_2019/html/Guo_SpotTune_Transfer_Learning_Through_Adaptive_Fine-Tuning_CVPR_2019_paper.html)[^6]. Transfer learning allows to fine-tuned a model trained in one task and apply it to another task. In Deep Learning, transfer learning is widely applied, but the strategy to conduct transfer learning depends on the dataset and the researcher.
SpotTune is an adaptive fine-tuning approach that finds the optimal fine-tuning strategy per instance for the target data. A handy method for your transfer learning tasks!

6. [Refining Coarse-grained Spatial Data using Auxiliary Spatial Data Sets with Various Granularities](https://arxiv.org/abs/1809.07952)[^7]. During my PhD I always had to use geographical data sources with various spatial aggregation (e.g. points, and district-level or city-level data). 
The usual way to deal with this problem it aggregating all the data to a common level. Researchers aggregated the data when the spatial aggregation of one dataset was lower than the target one, while they assume a uniform spatial distribution otherwise. 
This papers instead proposes a Gaussian process model that deals with datasets with varying spatial aggregations. Interesting!

7. [Tile2Vec: Unsupervised representation learning for spatially distributed data](https://arxiv.org/abs/1805.02855)[^8]. To be fair, I read this research some time ago from a [blog post of Sentiance](https://www.sentiance.com/2018/05/03/venue-mapping/), a US research company. 
However, this paper proposes a model that learns a latent vector (embedding) of a geographical place from its neighbouring images (e.g. Satellite). Thus, they use this unsupervised model to predict land cover, poverty and the health index of geographical areas.

8. [Uncovering the role of spatial constraints in the differences and similarities between physical and virtual mobility](https://arxiv.org/abs/1907.04122)[^9]. I recently had the chance of working on a dataset of app usage, and I published a paper in [Scientific Reports]() that studies the similarity between human mobility and app usage. In other words, in my view, human behavior is similar between the digital and physical worlds.
This paper discovers similar results in web browsing behaviour. From this paper, I especially liked the level of details in the comparisons and the fact that he is the first one comparing web browsing with mobility!
It was unfortunate that I did not read it before my paper.

9. [A public data set of spatio-temporal match events in soccer competitions](https://www.nature.com/articles/s41597-019-0247-7)[^10]. I now finish with two datasets. The first one is about football! Through this dataset, you can analyze the actions of football players during various International competitions. A UNIQUE dataset!

10. [Interaction data from the Copenhagen Networks Study](https://www.nature.com/articles/s41597-019-0325-x)[^11]. The Copenhagen Network study collected human interaction data from more than 700 university students. 
This data was passively collected, and it included phone calls, GPS locations[^12], Bluetooth proximity, and facebook friendships. After a careful operation of anonymization, the data is now available for everyone! Dig into it!

What are your favorite research papers of 2019?



[^1]: Rolnick, David, et al. "Tackling Climate Change with Machine Learning." arXiv preprint arXiv:1906.05433 (2019).
[^2]: Schwartz, Roy, et al. "Green AI." arXiv preprint arXiv:1907.10597 (2019).
[^3]: Perra, Nicola, and Luis EC Rocha. "Modelling opinion dynamics in the age of algorithmic personalisation." Scientific reports 9.1 (2019): 7261.
[^4]: Merity, Stephen. "Single Headed Attention RNN: Stop Thinking With Your Head." arXiv preprint arXiv:1911.11423 (2019).
[^5]: Kingma, Diederik P., and Max Welling. "Auto-encoding variational bayes." arXiv preprint arXiv:1312.6114 (2013).
[^6]: Guo, Yunhui, et al. "SpotTune: transfer learning through adaptive fine-tuning." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2019.
[^7]: Tanaka, Yusuke, et al. "Refining coarse-grained spatial data using auxiliary spatial data sets with various granularities." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 33. 2019.
[^8]: Jean, Neal, et al. "Tile2Vec: Unsupervised representation learning for spatially distributed data." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 33. 2019.
[^9]: Hazarie, Surendra, et al. "Uncovering the role of spatial constraints in the differences and similarities between physical and virtual mobility." arXiv preprint arXiv:1907.04122 (2019).
[^10]: Pappalardo, Luca, et al. "A public data set of spatio-temporal match events in soccer competitions." Scientific data 6.1 (2019): 1-15.
[^11]: Sapiezynski, Piotr, et al. "Interaction data from the Copenhagen Networks Study." Scientific Data 6.1 (2019): 1-10.
[^12]: For anonymity reasons, the GPS data is not shared in this dataset.

