GAMBIT's Website
----------------

For tutorials, documentation, and information, visit https://gambitbsm.github.io/.

## Project progress

Completed:
- Built new, clean website using Hugo and Doks, and migrated old content over
- Set up documentation generation using Doxygen, which is converted to markdown using Doxybook2
- Automated the process of updating the website using GitHub actions, including options to rebuild the Doxygen documentation and check for dead links
- Optimised website to handle the large number of pages
- Wrote a number of onboarding tutorials including an installation guide, an introduction to the GAMBIT interface, and a common problems page

ToDo:
- Add technical tutorials including introductions to the specific `Bits`
- Update the `make docs` command - this is used to generate local documentation similar to the automatic documentation on the site. However, it uses an outdated `Doxyfile` which could be updated to match the one in `/doxygen_and_doxybook2_config`
- Improve the way Doxybook2 is handled. Some parts of Doxybook2 had to be rewritten to fix issues with auto-generated links, and this source code is compiled and built when the automatic documentation is generated. This means documentation generation is slow - it would be better to store the modified Doxybook2 in a different repository
- Enable latex support to allow maths to be easily written

## Usage instructions

#### Structure
The website is built using the 0.5 beta version of the Hugo documentation theme Doks:
https://getdoks.org/


#### Editing the website

The user-generated pages are found in `/content/en`, and are stored as markdown files in a tree structure. These files can be easily added/edited/deleted, but make sure to follow the correct structure and add the right options to the frontmatter if you want a page to show up in a menu. To add a page you need to use the command `hugo new /content/en/path/to/new/page/new_page.md`. Images are stored in `/static/images`.

You can host the website locally to see the changed you make in real-time. Make sure you have `hugo` installed, and then in your cloned repo run:

```
hugo serve
```

Or alternatively:

```
npm install
npm run start
```

If you need to remove the `package-lock.json` and the generated `node_modules` folder run 
```
npm run clean:install
```
before re-installing packages with npm.

When the site has been built locally, you can then access the website via a web browser at `localhost:1313`. When pushing to the repo, make sure to only edit the `master` branch; the `gh-pages` is only used for deploying the website.

**Note that for some reason the generated documentation in `Documentation > Code Reference` does not work properly when running the website locally.**

#### Deploying the website

Once you have updated the `master` branch, you can deploy these changes using GitHub actions. Navigate to the `Actions` tab and then the `Deploy Gambit Site` action. Click `Run workflow`. You will be given the option of rebuilding the Doxygen documentation at the same time as deploying the site - note that this will increase deployment time considerably. If you do this then you should also make sure that the release repo address is up to date.

After this workflow has run then the GitHub workflow `pages build and deployment` should trigger automatically, along with `Check links`. If this does not happen then you may need to re-run the workflow. The `Check links` work flow will give you all the dead links on the website, along with the errors that they throw. Note that arxiv links always seem to register as broken because of their automatic bot detection.

Once these workflows have finished, the updated website should be available [here](https://gambitbsm.github.io/).
