# EdgarRenderer
EDGAR Renderer enables investors to view the interactive data filings submitted under the US Security and Exchange Commission 
(SEC) rules that require the use of XBRL via the SEC website. 

EDGAR Renderer was created by staff of the U.S. Securities and Exchange Commission. 

Data and content created by government employees within the scope of their employment are not subject to 
domestic copyright protection. 17 U.S.C. 105.

End user support is by e-mail direct to SEC at: Ask-OID@sec.gov

Developer issue management is by the Jira Edgar Renderer project: https://arelle.atlassian.net/projects/ER

This plugin branch was branched from the SEC-contributed master by Mark V Systems, and can be loaded as a plugin to Arelle in the normal manner.  E.g., if running from command line, --plugins  {path to here}/EdgarRenderer

To debug under eclipse, check this project out under arelle's plugin directory or soft link from EdgarRenderer to the Arelle project src/arelle/plugin directory, e.g., under MacOS/Linux:
    ln -s {path to here}/EdgarRenderer {path to arelle project}/src/arelle/plugin
    
To use this plugin securely without leaving any xbrl files on a server (such as a REST server, when processing SEC filings that represent non-public insider information) pass in a zip file as the input, and return a zip file as the output.  The modifications to make EdgarRenderer into a plugin won't use any disk storage for such a session of EdgarRenderer.  If installed as a localhost webserver or as a cgi-bin, then it could be run by REST interface:

    curl -X POST "-HContent-type: application/zip" 
         -T inputfiling.zip 
         -o outresults.zip 
         "http://localhost:8080/rest/xbrl/validation?efm-pragmatic&media=zip&plugins=EdgarRenderer"


Further notes on usage are in the __init__.py module comments.