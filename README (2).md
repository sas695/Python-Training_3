<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>Programming Assignment 3: Go Fish</h1>
<ul>
<li>Fundamentals of Modern Software - Fall 2019</li>
<li>Due September 25 by 11:59 PM</li>
</ul>
<h2>Introduction</h2>
<p>The goals of this assignment are:</p>
<ol>
<li>To give you more practice with loops, strings, lists, and dictionaries.</li>
<li>To ensure that you are familiar with functions.</li>
</ol>
<p><strong>REMINDERS</strong></p>
<ol>
<li><strong>When you are done, be sure to submit your work.</strong></li>
<li><strong>You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.</strong></li>
<li><strong>Be sure to test your programs thoroughly on a wide range of inputs. We will.</strong></li>
<li>**Your programs' output should match the output in the samples to the best of your ability (taking into account that the elements of random chance and player input in the Go Fish problem mean that two different playthroughs are very unlikely to coincide exactly).</li>
<li><strong>We have provided you with 'stub' programs that you can &ndash; and should &ndash; use as a starting pont.</strong></li>
</ol>
<h2>functions.py</h2>
<p>Implement the following functions:</p>
<pre><code>squareplustwo(n)
</code></pre>
<p>Returns the square of <code>n</code>, plus 2.  For example, <code>squareplustwo(10)</code> is <code>102</code>.</p>
<pre><code>ispalindrome(s)
</code></pre>
<p>Returns <code>True</code> if the string <code>s</code> is a palindrome &ndash; i.e., it reads the same backwards as it does forwards &ndash; and <code>False</code> otherwise. For example, <code>ispalindrome('embargo')</code> is <code>False</code>, and <code>ispalindrome('cabbagegabbac')</code> is <code>True</code>.</p>
<pre><code>secondgreatest(l)
</code></pre>
<p>Returns the value of the second-greatest integer in the list <code>l</code>.  (You can assume that each element of <code>l</code> is an integer.)  For example, <code>secondgreatest([1,5,4,2,3])</code> is <code>4</code>.</p>
<pre><code>flip(d)
</code></pre>
<p>Returns a dictionary that flips the keys and values from <code>d</code>.  For example, <code>flip({'alpha':10, 'beta':20, 'gamma':30})</code> is <code>{10:'alpha', 20:'beta', 30:'gamma'}</code>.  If there are two keys in <code>d</code> that have the same value, <code>flip</code> should return <code>None</code>.  For example, <code>flip({'alpha':10, 'beta':20, 'gamma':10})</code> is <code>None</code>.</p>
<pre><code>weightedsum(l,d)
</code></pre>
<p>You can assume that <code>d</code> is a dictionary defining the <em>weights</em> of the elements of <code>l</code>: that is, each element <code>e</code> in <code>l</code> is a key in <code>d</code>, and the weight is the value associated with <code>e</code> in <code>d</code>.  This function returns the total weights of all of the elements of <code>l</code>.  For example, <code>weightedsum([1,2,3,2,1], {1:5.0, 2:0,3:1.2}</code> is <code>5.0 + 0 + 1. + 0 + 5.0 = 11.2</code>.</p>
<h2>gofish.py</h2>
<p>Write a program that plays the card game Go Fish with the user.  Here are the rules of the game, along with some implementation notes:</p>
<ul>
<li>Our version of Go Fish is for 2 players: one human and one AI.  The human always plays first.</li>
<li>Our version of Go Fish is played with a deck of 40 cards.  There are 4 each of goldfish, catfish, trout, grouper,  tuna, salmon, sturgeon, piranha, swordfish, and clownfish.  You can represent each card as a string with the appropriate name, e.g. <code>'goldfish'</code>.</li>
<li>The deck is shuffled into a random order before play begins.</li>
<li>Each player is dealt an initial <em>hand</em> of 7 cards at random.  The remaining cards form the <em>draw pile</em>.</li>
<li>If at any time (including at the start of the game) a player has two matching cards in their hand (e.g., two sturgeon), they form a <em>pair</em>. The player immediately discards the pair from their hand and puts the pair in their <em>collection</em>.</li>
<li>On their turn, a player asks another player of their choice, &ldquo;Do you have any [blank]?&rdquo; and names a fish from their own hand.  Your program should prompt the player to choose a card to ask for.  On its turn, the AI should choose a card to ask for at random.</li>
<li>If the player being asked has one of the requested cards in their hand, they give it to the asking player (who now has a pair and should discard and score it).  The asking player takes another turn.</li>
<li>If the player being asked does not have the requested card in their hand, they say &ldquo;Go fish!&rdquo;  The asking player draws the top card from the draw pile.  Even if it forms a pair, they do not take another turn.</li>
<li>Each pair of cards has a <em>value</em> which represents the number of points it is worth.  The values are:</li>
<li>goldfish: 1</li>
<li>catfish: 1</li>
<li>trout: 1</li>
<li>grouper: 1</li>
<li>tuna: 2</li>
<li>salmon: 2</li>
<li>sturgeon: 2</li>
<li>piranha: 3</li>
<li>swordfish: 4</li>
<li>clownfish: -1</li>
<li>A player's <em>score</em> is the total of the values of the cards in their collection.</li>
<li>The game ends when either (a) one player is out of cards, or (b) the draw pile is out of cards.  Any remaining pairs in players' hands are placed in their collections.  The player with the highest score wins.</li>
</ul>
<p>There is a sample transcript of the program's output in <code>transcript.txt</code>. Note that the bulk of your grade will be based on correctly implementing the rules of Go Fish; focus on formatting the output correctly only once you have the gameplay code working.  (That said, if you have persistent difficulty getting an output to match, it may be an indication that there is something off about your program's logic.)</p>
<p><em>Hints: Do <code>functions.py</code> first. You will need to use the <code>random</code> module, as in the Fill-in-the-Blanks program from Lab 2. The demonstration program in Lab 3 will be a simpler interactive game, so you may find that helpful as a starting point.</em></p>
</div>