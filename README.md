
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
