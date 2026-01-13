---
title: Markdown Display Test
date: 2012-11-25
updated: 2021-04-18
version: 1.2.1
tags:
  - markdown
  - test
author: MinchinWeb
category: test
image: images/birger-strahl-olI66vtMgNo-unsplash.jpg
---

<div id="contents"></div>

This file serves three purposes:  
1) a markdown language reference,  
2) a test file to ensure that the markdown is being interpreted propertly, and  
3) a place to test out changes to the accompanying CSS file (`md-styles.css`).

Let us begin:

# Table of Contents (JS)

Include an empty div with `id="contents"` at start of file to have a floating 
table of contents automatically generated. eg:

~~~html
<div id="contents"></div>
~~~

The Table of Contents div scrolls down with the page and is generated from headers.
This is generated through the use of JavaScript and is not (directly) a part of
Markdown.

# Headers

Hashmarks on the right are optional.

~~~md
# Header 1
## Header 2
### Header 3 ###    <!-- Hashes on right are optional -->
#### Header 4
##### Header 5
###### Header 6
~~~

# Header 1

## Header 2

### Header 3 ###

#### Header 4

##### Header 5

###### Header 6

~~~md
## Markdown plus h2 with a custom ID ##         {#id-goes-here}

[Link back to H2](#id-goes-here)
~~~

## Markdown plus h2 with a custom ID ##         {#id-goes-here}

[Link back to H2](#id-goes-here)

Alternatively, for H1 and H2, an underline-ish style:

~~~md
Alt-H1
======

Alt-H2
------
~~~

Alt-H1
======

Alt-H2
------

# Paragraphs

~~~md
This is a paragraph, which is text
surrounded by whitespace. Paragraphs
can be on one line (or many), and can
drone on for hours.
~~~

This is a paragraph, which is text
surrounded by whitespace. Paragraphs
can be on one line (or many), and can
drone on for hours.

~~~md
Text with  
two trailing spaces  
(on the right)  
can be used  
for things like poems  
~~~

Text with  
two trailing spaces  
(on the right)  
can be used  
for things like poems  

~~~md
Now some inline markup like _italics_,
**bold**, and `code()`. Note that
underscores in the middle of words are
ignored in Markdown Extra.
~~~

Now some inline markup like _italics_,
**bold**, and `code()`. Note that
underscores in the middle of words are
ignored in Markdown Extra.

~~~md
> Blockquotes are like quoted text
> in email replies
>> And, they can be nested
>>> Level three
~~~

> Blockquotes are like quoted text
> in email replies
>> And, they can be nested
>>> Level three

~~~md
<div class="custom-class" markdown="1">
This is a div wrapping some Markdown
plus.  Without the DIV attribute (the
`markdown=1` part), it ignores the block. 
</div>
~~~

<div class="custom-class" markdown="1">
This is a div wrapping some Markdown
plus.  Without the DIV attribute (the
`markdown=1` part), it ignores the block.
</div>

# Links

~~~md
Here is a Markdown link to
[Google](http://google.com).
~~~

Here is a Markdown link to
[Google](http://google.com).

~~~md
This is [an example][id] reference-method link.

[id]: http://example.com/ "Optional Title Here"
~~~

This is [an example][id] reference-method link.
  
[id]: http://example.com/ "Optional Title Here"

References (the `[id]` part) do not need to follow immediately after the
link. In fact, I think most people gather them at the end of the document.

~~~md
<http://example.com/>  
<address@example.com>
~~~

<http://example.com/>  
<address@example.com>

As a bonus, email addresses are automatically obscured. Notice that web
addresses need to be in angle brackets to turn into links. Markdown does
not otherwise contain automatic link and address detection.

# Images

~~~md
![Alt text](/path/to/img.jpg "Image call example")
![Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg "Title")
![Alt text][img1]
[img1]: /path/to/img.jpg "Title"
~~~

![Alt text]({static}images/sample.png "Image call example")
![Alt text]({static}images/sample.png)
![Alt text]({static}images/sample.png "Title")
![Alt text][img1]
[img1]: {static}images/sample.png "Title"

# Lists

Use *, +, or - to create a list. Use numbers to create a numbered list.
The actual numbers used are ignored at the present time.

~~~md
* Bullet lists are easy too
- Another one
+ Another one

. <!-- somthing to break between the lists... -->

1. A numbered list
2. Which is numbered
3. With periods and a space
100. Who said we could count?
~~~

* Bullet lists are easy too
- Another one
+ Another one

.

1. A numbered list
2. Which is numbered
3. With periods and a space
100. Who said we could count?

# Code

Code can be intended.

~~~md
    // Code is just text indented a bit like this
    which(is_easy) to_remember();
~~~

    // Code is just text indented a bit like this
    which(is_easy) to_remember();

Code can be marked off with ~~~ above and below the block. A langauge can be
specified so that it is highlighted "correctly". Most blocks in this document
are `md` (for *markdown*).

~~~md
~~~cpp
// Markdown extra adds un-indented code blocks too

if (this_is_more_code == true && !indented) {
    // tild wrapped code blocks, also not indented
}
\~~~
~~~

~~~cpp
// Markdown extra adds un-indented code blocks too

if (this_is_more_code == true && !indented) {
    // tild wrapped code blocks, also not indented
}
~~~
<!-- _ this is just to make it display nice is Notepad++ -->

Code can be inline:

~~~md
Use `<div>` tags
`echo uname -a`
~~~

Use `<div>` tags  
`echo uname -a`

# Horizontal rules

~~~md
* * * *
****
- - -
~~~

* * * *
****
- - -

Paragraphs following a horizontal rule will have a drop cap for the first
character. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Mauris quis augue tortor, in accumsan urna. Sed 
vestibulum, augue at commodo ultricies, leo libero faucibus lorem, nec 
porta eros massa quis nunc.

# Tables (Markdown-Plus)

~~~md
| Header | Header | Right  |
| ------ | ------ | -----: |
|  Cell  |  Cell  |   $10  |
|  Cell  |  Cell  |   $20  |
~~~

| Header | Header | Right  |
| ------ | ------ | -----: |
|  Cell  |  Cell  |   $10  |
|  Cell  |  Cell  |   $20  |

* Outer pipes on tables are optional
* Colon used for alignment (right versus left)

# Definition Lists (Markdown-Plus)

~~~md
Bottled water
: $ 1.25
: $ 1.55 (Large)

Milk
Pop
: $ 1.75
~~~

Bottled water
: $ 1.25
: $ 1.55 (Large)

Milk
Pop
: $ 1.75

* Multiple definitions and terms are possible
* Definitions can include multiple paragraphs too

# Abbreviations (Markdown-Plus)

~~~md
Hover over this here [ABBR] (a tooltip should
show up)

*[ABBR]: Markdown-Plus abbreviations (produces an <abbr> tag)
~~~

Hover over this here [ABBR] (a tooltip should show up)

*[ABBR]: Markdown-Plus abbreviations (produces an <abbr> tag)

Your list of abbreviations is often collected at the bottom of the source
document (with footnotes.)

# Footnotes (Markdown-Plus)

~~~md
That's some text with a footnote.[^1]

[^1]: And that's the footnote.
~~~

That's some text with a footnote.[^1]

[^1]: And that's the footnote.

Note that footnotes show up at the bottom of the page, with a
link back to its place in the original text.
Note that two footnotes cannot have the same "name".

Your list of footnotes is often collected at the bottom of the source
document (with abbreviations.)

# Literal Characters

The following characters sometimes have special meanings in Markdown. You
can make sure Markdown doesn't interpret these characters by placing a
backslash in front of them.

* \\  -- backslash
* \`  -- backtick
* \*  -- asterisk
* \_  -- underscore
* \{\} -- curly braces
* \[\] -- square brackets
* \(\) -- parentheses
* \#  -- hash mark
* \+  -- plus sign
* \-  -- minus sign (hyphen)
* \.  -- dot
* \!  -- exclamation mark
* \:  -- colon
* \|  -- pipe

~~~md
\\  \`  \*  \_  \{\} \[\] \(\) \#  \+  \-  \.  \!  \:  \| 
~~~

\\  \`  \*  \_  \{\} \[\] \(\) \#  \+  \-  \.  \!  \:  \|  

# SmartyPants

SmartyPants transforms:

* straight quotes (`"` and `'`) in "curly" 'quotes'
* Backtick quotes into ``curly'' quotes
* Dashed in en- and em- dashes: -- and ---
* Three consecutive dots in an ellipsis: ...
* Adds unbreakable spaces
    * before a colon :  
    * before a semicolon ;
    * before an exclamation mark !
    * before a question mark ?
    * inside << French style quotes >>
    * as the thousand seperator 100 000
    * between a value and common unit symbols  12 kg  and 10 °C

# MathJax

(If) math display via MathJax has been activated, allowing the typing of math
formulas. For more information about MathJax: <http://www.mathjax.org/>. For
more information on how to use this:
<https://github.com/drdrang/php-markdown-extra-math>. In general formulas are
encapsulated by \ ( and \ ) or \ [ and \ ].

Formulas can be inline

~~~latex
where \(\alpha = (t_1 - t_0)/L\) is the rate at which the thickness increases
~~~

where \(\alpha = (t_1 - t_0)/L\) is the rate at which the thickness increases

Some other samples:

~~~latex
\[\sqrt{x^2+1}\]

\(\root 3\of {1-\pi x^2}\)

\[\overbrace{x+\cdots+x}^{k\;\rm times}\]

\(f(x)=\cases {
    x^2+1&\text{if $x<0$}\cr
    1-x&\text{otherwise}
}\)

\(\left[\matrix{a^2-b^2& -1\\ 1& 2ab}\right]\)
~~~

\[\sqrt{x^2+1}\]

\(\root 3\of {1-\pi x^2}\)

\[\overbrace{x+\cdots+x}^{k\;\rm times}\]

\(f(x)=\cases {
  x^2+1&\text{if $x<0$}\cr
  1-x&\text{otherwise}
}\)

\(\left[\matrix{a^2-b^2& -1\\ 1& 2ab}\right]\)

~~~latex
\(\int^1_\kappa
\left[\bigl(1-w^2\bigr)\bigl(\kappa^2-w^2\bigr)\right]^{-1/2} dw
= \frac{4}{\left(1+\sqrt{\kappa}\,\right)^2} K
\left(\left(\frac{1-\sqrt{\kappa}}{1+\sqrt{\kappa}}\right)^{\!\!2}\right)\)
~~~

\(\int^1_\kappa
\left[\bigl(1-w^2\bigr)\bigl(\kappa^2-w^2\bigr)\right]^{-1/2} dw
= \frac{4}{\left(1+\sqrt{\kappa}\,\right)^2} K
\left(\left(\frac{1-\sqrt{\kappa}}{1+\sqrt{\kappa}}\right)^{\!\!2}\right)\)

~~~latex
\(\mathop{\rm grd} \phi(z) =
\left(a+\frac{2d}{\pi}\right) v_\infty\, \overline{f'(z)} =
v_\infty \left[ \pi a + \frac{2d}{\pi a + 2dw^{-1/2}(w-1)^{1/2}} \right]^-\)
~~~

\(\mathop{\rm grd} \phi(z) =
\left(a+\frac{2d}{\pi}\right) v_\infty\, \overline{f'(z)} =
v_\infty \left[ \pi a + \frac{2d}{\pi a + 2dw^{-1/2}(w-1)^{1/2}} \right]^-\)

<div class="col2" markdown="1">
# 2 Column Display

This is text that is supposed to be displayed in
2 columns. Invoke columns by using:

~~~html
<div class="col2" markdown="1">
text here
</div>
~~~

Markdown will be rendered. `<H1>`, `<H2>`, and `<hr>` will span both columns.
This is not a function of the Markdown, but rather the stylesheet.

...

# Two Column Break ============ &

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas in pretium metus.
Cras tempor lacinia risus in porttitor. In hac habitasse platea dictumst. Proin
auctor nibh in metus condimentum ut lacinia magna rhoncus.

Donec non enim id
dolor elementum tincidunt. Fusce et quam nulla. Vivamus diam lacus, ultrices
quis malesuada ullamcorper, elementum in elit.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et leo ac libero 
pellentesque volutpat. Nunc euismod fermentum augue, vel laoreet ante gravida nec.
Etiam et odio ac ante interdum adipiscing.

Ut gravida nulla at erat accumsan quis
fermentum est sagittis. Suspendisse dignissim congue nibh, quis porttitor magna
dignissim at. Sed ut eros est.

## Another Two Column Break ================ &

Maecenas dictum sodales leo in sagittis. Sed ullamcorper enim nec ligula tempus
eu gravida enim laoreet. Nunc eu feugiat erat.

***

Morbi interdum, nisl at fringilla
semper, magna lorem laoreet neque, ac posuere risus diam et odio. Mauris iaculis
aliquet augue, vel ullamcorper massa rutrum pulvinar. Curabitur nisi orci,
molestie egestas dignissim eget, suscipit vel nunc.

Praesent aliquam tempor
lectus, sed facilisis urna aliquam non. Nulla facilisi.

***

Aenean at tellus velit. Aliquam eleifend cursus posuere. Sed semper, justo
lacinia pharetra ultricies, nulla purus tincidunt enim, non pretium odio ante
eget velit. Cras luctus dolor vitae eros mattis hendrerit.

Vivamus quis erat nec tellus
vehicula placerat. Class aptent taciti sociosqu ad litora torquent per conubia
nostra, per inceptos himenaeos.
</div>

# For more information

* Markdown Handler for Apache (this project) - <https://github.com/MinchinWeb/markdown-handler>
* Markdown - <http://daringfireball.net/projects/markdown/syntax>
* Markdown Plus - <http://michelf.ca/projects/php-markdown/extra/>
* SmartyPants (in php) - <http://michelf.ca/projects/php-smartypants/>
* MathJax - <http://www.mathjax.org/>
* jsMath (an alternative to MathJax) - <http://www.math.union.edu/~dpvc/jsmath/>
* Markdown and MathJax - <https://github.com/drdrang/php-markdown-extra-math>

# Image Credit

Header photo by [Birger Strahl](https://unsplash.com/@bist31).
