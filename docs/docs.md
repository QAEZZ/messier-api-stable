<!DOCTYPE html>
<html>
    <body style="background-color:#363636;">
        <div id="wrapper">
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
            <h3>Go to <a href="https://messier-api.russiandev.repl.co">messier-api.russiandev.repl.co</a> for a more detailed doc with extra features.</h3>
    </body>
</html>
