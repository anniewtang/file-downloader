# file-downloader

### PURPOSE + CAVEATS
<p><ul>
    <li> providing a base script to easily/quickly download links from the internet.</li>
    <li> offers the following interactive, simple command-line features:
      <ul>
        <li>lets the user choose whether or not they want to manually verify which files to save/download, during the script</li>
        <li>also offers the option of just "blindly" downloading all the links that the webpage contained</li>
        <li>lets the user quit during the middle of the webscrape</li>
      </ul>
    </li>
    <li> users must (currently) be at least familiar with html, file paths, and (hopefully minimally) python in order to
         customize the script to their particular website html</li>
    <li> currently only works for websites that have their files stored under the same domain as the main webpage (a TODO for me to 
         change)</li>
  </ul>
</p>
  
### INSTRUCTIONS: SETTING UP THE SCRIPT
<p> 
  NOTE: users can refer to <code>sample.py</code> for an example of how to fill out the base script. <br>
  Certain variables/conditions might change or are unneeded, depending on how the webpage is set up. <br>
  Before using, make sure to follow these instructions to customize the script for your purposes!
  <ul>
    <li> <b>TODO: URL</b>  
      <ul>
        <li>whichever URL you're on to <i>inspect the html</i> should be the URL you assign to <code>url</code></li>
        <li>in the <code>sample.py</code>.py, you can see I have the main cs170 website URL assigned to <code>url</code></li>
        <li>note: make sure that your URL ends with <code>/</code>, if your file URL is nested under the main webpage</li>
      </ul>
    </li>
    <li> <b>TODO: EXTENSION</b>
      <ul>
        <li>for the cs170 website, the links to the files weren't actually stored in the html file for the main webpage</li>
        <li>instead, the links were written in a separate html file, which was nested under the main webpage's html</li>
        <li>hence, i included an <code>extension</code> variable, to add onto the original URL to appropriately scrape the links</li>
        <li>if your links are located in the main html, you can leave the <code>extension</code> variable as is</li>
        <li>another note: in line 49, where we're <i>constructing</i> the URL our script will use to grab the files,
            it's important to observe where your file links are stored. for cs170, although the link references were 
            written in the <code>calendar.html</code> file, the links themselves were in an <code>assets</code> folder,
            which had to be accessed through the main <code>url</code> (doesn't involve <code>calendar.html</code>). 
            adjust this construction according to your situation!</li>
      </ul>
    </li>
    <li><b>TODO: TAG</b>
      <ul>
        <li>while inspecting your DOM/page source, determine which html tag best indicates/narrows down where the code
            for the links are located</li>
        <li>if it's a regular HTML tag, you can just put the tag type (i.e. <code>'a'</code> or <code>'p'</code>). 
             however, if it's a specific class or id you want to reference, assign it to the <code>tag</code> variable
             as the following: <code>'class_=results'</code>, or <code>'id=results'</code>. 
             you can google for more formats/information on how BeautifulSoup handles <code>find()</code> and <code>find_all()</code></li>
      </ul>
    </li>
    <li> <b>TODO: KEYWORD</b>
      <ul>
        <li>for cs170, the links that were found included a lot of random links that didn't have to do with the files
            i was interested in.</li>
        <li>to take care of that, i had a <code>keyword</code> variable, that allowed me to determine whether or not
          the link retrieved was related to the types of files i wanted to download</li>
        <li>for you, if you have a similar situation, make sure the <code>keyword</code> you assign is the starting portion of
          the URL that would help filter out unrelated links</li>
        <li>additionally for cs170, the links given were file extensions (i.e. <code>assets/disc/...</code>) that would
          be added to the end of the main <code>url</code>, vs. being full links themselves</li>
        <li>as each website may be implemented differently, this is something you should be aware of as well and might
          have to adjust when it comes to constructing the URL and pre-emptively checking for validity (if you want to)</li>
      </ul>
    </li>
    <li> <b>TODO: PATH</b>
      <ul>
        <li>the <code>path</code> variable is so the script (which uses <code>wget</code>) knows where to save the files</li>
        <li>to find the exact, <b>full</b> path you want your files to be saved to, if you're on mac, you can follow these steps:
          <ul>
            <li><b>STEP 1:</b> if you're familiar with the terminal, you can directly navigate to the folder you want in your terminal
                and skip to STEP 6. i recommend still following STEP 6 and onwards, just to safe-check that you have the correct
                <i>full</i> path.
                otherwise, if you're not that comfortable with the terminal, you can move ahead to STEP 2</li>
            <li><b>STEP 2:</b> navigate to the folder you want to save your files to in your <code>Finder</code></li>
            <li><b>STEP 3:</b> hit <code>command + spacebar</code> to open up spotlight search</li>
            <li><b>STEP 4:</b> type in <code>terminal</code> into the search, and open up a new terminal window.</li>
            <li><b>STEP 5:</b> go to your finder, and drag your folder onto the <code>terminal</code> <i>app icon</i> that's located in
                your dock! not the terminal window itself</li>
            <li><b>STEP 6:</b> now that you have the correct path loaded in your terminal, it should look something like this:
              <code>Mackbook:folder-name UserName$</code></li>
            <li><b>STEP 7:</b> now enter the following command: <code>pwd|pbcopy</code>. what this just did was copy the current path
                into your clipboard. you can alternatively do: <code>pwd</code>, and manually copy the path yourself by 
                just <code>cmd+c</code></li>
            <li><b>STEP 8:</b> paste the path into the <code>path</code> variable in our file. make sure that there are no extraneous
                line breaks, which may occur if you chose to use the <code>pbcopy</code> shortcut.</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</p>

### INSTRUCTIONS: RUNNING THE SCRIPT
To run the script, and to utilize the interactive features I built into it, just navigate to the path in your terminal of the folder
that you've saved the <code>flexible-downloads.py</code> file in. <br>
Enter the following command: <code>python3 flexible-downloads.py</code>, and follow the user prompts!

  
    
