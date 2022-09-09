<!DOCTYPE html>
<html>
    <body style="background-color:#363636;">
        <div id="wrapper">
            <footer class="w3-container w3-dark-white" style="padding:30px"></footer>
            <!-- <img style="position:flex;width:10%;top:100px;z-index:-1;" src="https://media.sciencephoto.com/image/v7000261/800wm/V7000261-Sketch_of_Andromeda_by_Messier,_1807.jpg"> -->
            <h2 class="messier-api-typeout" id="messier-api-typeout" style="position:flex;left:135px;top:-90px;"></h2>
            <!-- <span class="cursor"> |</span> -->
            <div id="about-typeout">
                <span style="position:flex;left:137px;top:-115px;font-size: medium;"><i></i></span>
            </div>
            <br/>
            <!-- <p style="position:flex;left:137px;top:-130px;">the API currently features things that do stuff</p> -->
            <div class="topnav w3-top">
                <a class="active" onclick="location.reload();return false;" style="background-image:url(https://media.sciencephoto.com/image/v7000261/800wm/V7000261-Sketch_of_Andromeda_by_Messier,_1807.jpg);background-repeat:no-repeat;background-size:cover;color:rgba(0, 0, 0, 0)">.....</a>
                <a href="https://messier-api.russiandev.repl.co/messier">/messier</a>
                <a href="https://github.com/QAEZZ/messier-api">GitHub</a>
                <a href="#languageSel">Examples</a>
                <a href="#methodSel">Link Gen</a>
            </div>
            <div>
                <table>
                    <tr class="th-bg">
                        <th>Base URL</th>
                    </tr>
                    <tr class="td-bg">
                        <td>https://messier-api.russiandev.repl.co</td>
                    </tr>
                </table>
            </div>
            <br/>
            <div>
                <table>
                    <tr class="th-bg">
                        <th>Type</th>
                        <th>URL</th>
                        <th>Parameters</th>
                        <th>Description</th>
                    </tr>
                    <tr class="td-bg">
                        <td>GET</td>
                        <td>/messier</td>
                        <td>optional: object, format</td>
                        <td>Gateway to the main part of the API</td>
                    </tr>
                    <tr class="td-bg">
                        <td>GET</td>
                        <td>/messier/random</td>
                        <td>optional: format</td>
                        <td>Returns data on a random object</td>
                    </tr>
                    <tr class="td-bg">
                        <td>GET</td>
                        <td>/messier/all</td>
                        <td>optional: format</td>
                        <td>Returns the whole JSON file</td>
                    </tr>
                    <tr class="td-bg">
                        <td>POST</td>
                        <td>/convertHashmapJson</td>
                        <td>required: json, hashmap</td>
                        <td>Converts hashmap to json and vice-versa</td>
                    </tr>
                </table>
                <br/>
                <h3>/messier parameters</h3>
                <table>
                    <tr class="th-bg">
                        <th>Parameters</th>
                        <th>Value</th>
                        <th>Description</th>
                        <th>Example</th>
                    </tr>
                    <tr class="td-bg">
                        <td>?object</td>
                        <td>int</td>
                        <td>Returns information on a certain object</td>
                        <td>/messier?object=104</td>
                    </tr>
                    <tr class="td-bg">
                        <td>?format</td>
                        <td>str: xml, yaml, html, visual</td>
                        <td>Returns information in a certain format, the API defaults to JSON if you don't define a type. (So <b>don't</b> set <i>?format=json</i>)</td>
                        <td>/messier?object=104&format=xml</td>
                    </tr>
                </table>
            </div>
            <br/>
            <div>
                <p>Example response from <i class="reverse-highlight">https://messier-api.russiandev.repl.co/messier?object=104</i></p>
                <div class="codebox">
                    <pre>
                        <code>
{
    "M":104,
    "NGC":"NGC 4594 Sombrero Galaxy",
    "TYPE":"Spiral Galaxy",
    "CONS":"Virgo",
    "RA":"12h 40m",
    "DEC":"-11\u00b037",
    "MAG":8,
    "SIZE":"9x4",
    "DIST (ly)":"50,000,000",
    "VIEWING SEASON":"Spring",
    "VIEWING DIFFICULTY":"Easy",
    "PHOTO":"https://www.messier-objects.com/wp-content/uploads/2015/09/Messier-104.jpg"
}
                        </code>
                    </pre>
                </div>
            </div>
            <br/>
            <div style="position:flex;top:70px">
                <!-- move to the top left corner underneath the top nav bar-->
                <label style="color: white">
                    Choose a language:<br/>
                    <select id="languageSel" class="languageSelectClass" name="languageSelect" style="background-color: #c3c3c3;">
                        <option value="Python">Python</option>
                        <option value="cURL">cURL</option>
                        <option value="Axios">JavaScript (Axios)</option>
                        <option value="HttpClient">C# (HttpClient)</option>
                    </select>
                </label>
                <div class="output codebox"></div>
                <br/>
                <label style="color: white">
                    Choose a method:<br/>
                    <select id="methodSel" class="methodSelectClass" name="methodSelect" style="background-color: #c3c3c3;">
                        <option value="none">none</option>
                        <option value="object">?object</option>
                        <option value="random">/random</option>
                        <option value="all">/all</option>
                        <option value="convertHashmapJson">/convertHashmapJson</option>
                    </select>
                </label>
                <div class="ezCodeOutput codebox"></div>
                <footer class="w3-container w3-dark-white" style="padding:10px"></footer>
                <div class="toTopButton">
                    <a href="#wrapper">Back to Top?</a>
                </div>
                <footer class="w3-container w3-dark-white" style="padding:40px"></footer>
            </div>
            <script type="text/javascript" src="https://messier-api.russiandev.repl.co/static/js/script.js"></script>
        </div>
    </body>
</html>
