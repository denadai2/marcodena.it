Title: Stop remembering passwords
Date: 2014-09-02 10:20
Category: Security
Thumb: mitro.png
Exceprt: Passwords are a "pain in the ass" and hackers continue stealing them. With a password manager like Mitro it's possible to stop remembering passwords and having the security of a bullet proof Open Source system.

Every day we hear about hackers stealing password and accounts. Just one week ago [1.2 billion passwords were stolen](http://it.slashdot.org/story/14/09/01/2213202/hackers-behind-biggest-ever-password-theft-begin-attacks), and [The Fappening](http://en.wikipedia.org/wiki/2014_celebrity_pictures_hack) hacker shown the content of the phone of Jennifer Lawrence, Selena Gomez, and many others. Nevertheless, we continue to trust somehow the __passwords__, which are insecure, we often forget them and, finally, we complain when someone hacks our E-mail or Facebook account. Ask yourself:

* What can happen and how much time will your waste with a stolen Facebook account? 
* Are you using the same password everywhere? If so, do you know how dangerous it is?

In this article, I will present one of the most secure methods to overcome the old password fashion.

<iframe width="637" height="358" src="//www.youtube.com/embed/vrQFBYgwQW8" frameborder="0" allowfullscreen></iframe>_Video: [The Fappening](http://en.wikipedia.org/wiki/2014_celebrity_pictures_hack) - Reddit reacting to Jennifer Lawrence nudes_

## Why is the same password method so insecure

Reusing passwords for email, banking, and social media accounts can lead to identity theft. Imagine an attacker who steals your Twitter account password. What happens if it is different from all the others? Now Imagine the contrary. 

(Extra: [is your password secure?](https://howsecureismypassword.net/). This method only checks the length of the password, comparing it with a normal PC attack. It is simplistic.)

## What's the solution

My solution is to use [Mitro](https://www.mitro.co/), a project that allows you to generate, store and use different passwords on the websites you normally use. Let me explain better: let's say you want to create a Facebook account. In this case, you go to the registration page, and Mitro will generate for you a password, which is very difficult and random. This password will be stored in Mitro and the next time you login on Facebook, it will fill the login form for you. __You don't even need to know your own password!!__ Mitro will also generate for you a truly random password, which is not dependent on any personal information or existing word.

![Mitro screenshot](/images/mitro.png)

I never trusted password managers: __what if someone hacks or find the list of my passwords?__ It's a single point of failure, right? With Mitro, this is theoretically not possible. As their [Security FAQ](https://www.mitro.co/secure.html) says: "Mitro is designed so that only you, and the people you share with, have access to your secrets. Your passwords never leave your computer without being encrypted, so no one, not even Mitro, has access to them". Great!!

From the moment I gave a try to Mitro, __I deleted all the cookies and changed all the passwords__ of the website I normally use. Mitro saved me!

Let's try!! First of all, I will change the password of Facebook, just to show you how the system works. I generate the password with Mitro, and I copy-paste it in the Facebook form. It's a strong password!

![Facebook change password](/images/stop-password1.png)
![Mitro password generator](/images/mitro-passowrd-generation.png)
![Facebook change password2](/images/stop-password2.png)

At this point I log in. In my case, I had a different password saved in Mitro so I will memorize the new one.

![Facebook login](/images/stop-password3.png)

Now, when you need to log in again in the website, Mitro will take care of the rest

![Mitro Facebook login](/images/stop-password4.png)

So you will not care about remembering passwords anymore, and your internet life will gain a new type of security. Don't you trust me? Try it on one website! Try to change a password and use Mitro from that moment, please! After this, share your thoughts with me, please. I'm curious/interested :)

__Mitro was recently bought by Twitter__. The extensions are for Chrome, Safari, and Firefox. There is also an iOS app.


## Why Mitro and not the others?

There are many other similar solutions, like [LastPass](https://lastpass.com/), so why did I choose Mitro? Especially after the NSA revelations, I seriously reconsidered Open Source in the security field. Open source allows people to read the code, understand if a company uses your information differently but it, also helps with getting more eyes on the code. The recent [Hearthbleed bug](http://heartbleed.com/) proved it: a super small modification in the code allowed a serious security bug which affected the 90% of the websites on Internet, including Facebook. If OpenSSL weren't Open Source the Heartbleed bug would probably have never been [discovered](http://en.wikipedia.org/wiki/Heartbleed#Discovery).

__Mitro is Open Source__: everyone can review/contribute the code in [this GitHub project](https://github.com/mitro-co/mitro). I personally do it.

Mitro even allows you to __run your own server__, if you don't trust the Mitro servers!

## Is it the future?

Yes and no. Mitro attacks the problem on the "password side": it allows you to use the websites in the old way, storing your passwords and increasing the security. The future will probably be about using different types of access methods, like [OAuth](http://oauth.net/), [Mozilla Persona](https://www.mozilla.org/en-US/persona/) or [considering obsolete the passwords](https://medium.com/@ninjudd/passwords-are-obsolete-9ed56d483eb). All these methods depend on the websites we use, so we can't do anything but wait. 

We just need to wait, using Mitro meanwhile.

Please, give it a try and share your thoughts :)








