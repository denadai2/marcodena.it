Title: Wordpress? The future is static
Date: 2014-08-09 10:20
Category: Programming

I was a PHP developer and I lived the blog fashion bubble when everyone made blogs, 
even talking about non-sense. Since that "era" [Wordpress](http://www.wordpress.org)
established the "standard de-facto" of the blogging platforms. Wordpress is highly
customizable (it has more than 15'000 of plugins), it is used by high profile
websites like [The New York Observer](http://www.observer.com/) and someone is even
using it as CMS.

As I said I am a developer since many years ago and I barely managed to build this
portfolio, because usually we have time for others but not for ourselves. Moreover I 
easily get tired: upgrades? bugs? exploits? I really can't handle all these things
anymore, also because I don't use Wordpress anywhere but here.

I also saw the evolution of Wordpress: from a small and not well written script, 
it became a fancy not well written OOP script. 

Here are some __cons about Wordpress__:

 * exploits! Do you have time to keep it updated? Do you really trust the auto-update
 feature? Be prepared to backup and restore everything.
 * __WYSIWYG?__ I never even liked to write within the administration panel: every time I needed to change the blog template (font), the WYSIWYG was displaying the horrible Times new roman font, misleading me about the real appareances of the post.
 * slow: do you really think that in the age when [Google incorporates site speed in search
 rankings](http://www.mattcutts.com/blog/site-speed/) you are safe? Are you thinking
 about having a high-traffic website? You don't have money to waste?

For all these reasons I came out with static site generators. After half a decade when
people were obsessed by dynamicity, we are finally going back to site generators like
[Jenkill](http://jekyllrb.com/), officially supported and [used by Github](https://github.com/blog/1867-github-pages-now-runs-jekyll-2-2-0) and [Pelican](http://blog.getpelican.com/), the script
used to generate this website. Even thought Jenkill is almost complete, I must admit
that I don't know Ruby and that I prefer the [Pelican documentation](http://docs.getpelican.com/en/3.4.0/index.html). Pelican is written in Python.

These are some __pro of Pelican__ (but they are applicable to all the static website generators):

 * fast! As it will be explained later, all the speed problems will be solved.
 * no database required. 
 * Users will use a simple text editor and [Markdown](http://daringfireball.net/projects/markdown/)
 syntax to write.
 * cheap and easy to host practically anywhere. Amazon S3 and [Github pages](http://pages.github.com/) (free)
 are the most used choices.
 * websites are easy to secure, maintain and scale.

## How to start
The best way to start is understanding how easy is to make a blog. The [quickstart](http://docs.getpelican.com/en/3.4.0/quickstart.html) is very comprensive. First of all some Python packages are necessary.

    pip install pelican markdown

The second step is generating the basic structure of the blog.

	:::python
    mkdir -p ~/projects/yoursite
    cd ~/projects/yoursite
    pelican-quickstart

Now it is time to write the __first article__ in Markdown:

	::Makefiles
    Title: My First Review
    Date: 2010-12-03 10:20
    Category: Review
    
    Following is a review of my favorite mechanical keyboard.
 
And save it to "~/projects/yoursite/content/keyboard-review.md". The "content"
directory is made for all the posts and pages and it will not change even if the
blog will be revolutionized.
From the "~/projects/yoursite/" directory, you can launch

    pelican content

The static HTML files will be generated in the output directory. To visit your new
website, just launch

    cd ~/projects/yoursite/output
    python -m SimpleHTTPServer

And navigate http://localhost:8000/ in your browser.

## Performances

I am a nerd, I like performances benchmarks. In this plot it is possible to find the performance
of Wordpress and Pelican in a simple hosting of gandi.net, but also Pelican (stati HTMLs) in Amazon S3.

![benchmarks](/images/benchmark.png)

__Notes:__ the tests are made with [Apache ab](http://httpd.apache.org/docs/2.2/programs/ab.html) via Internet,
so the performance is also affected by the speed of the connection and the congestion on the moment
of the test. The peak in the end is probably caused by this. I am sorry but I could not set up a local server in my PC. 

## Host your website for free

If you want to host a website for free, use Github pages. [Here](http://www.circuidipity.com/github-pages.html) you find a nice tutorial.

## Sources of this website

The sources of this website are available [here](https://github.com/denadai2/marcodena.it).





