var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const output = document.querySelector(".output");
const selectElement = document.querySelector(".languageSelectClass");
const ezCodeElement = document.querySelector(".methodSelectClass");
const ezCodeOutput = document.querySelector(".ezCodeOutput");
const PythonEx = 'from urllib.request import urlopen<br/>import json<br/><br/>url = "messier-api.russiandev.repl.co/messier/object/random"<br/>resp = urlopen(url)<br/>data = json.load(resp.read())<br/><br/>print(data)';
const cURLEx = "curl --request GET \\ <br/>    --location \\ <br/>    --url 'messier-api.russiandev.repl.co/messier?object=104'";
const AxiosEx = "import axios from \"axios\";<br/><br/>const options = {<br/>  method: 'GET',<br/>  url: 'messier-api.russiandev.repl.co/messier/random'<br/>};<br/><br/>axios.request(options).then(function (response) {<br/>   console.log(response.data);<br/>}).catch(function (error) {</br>   console.error(error);<br/>});";
const HttpClientEx = 'var client = new HttpClient();<br/>    var request = new HttpRequestMessage<br/>    {<br/>    	Method = HttpMethod.Get,<br/>    	RequestUri = new Uri("messier-api.russiandev.repl.co/messier/random"),<br/>    };<br/>    using (var response = client.SendAsync(request))<br/>    {<br/>    	response.EnsureSuccessStatusCode();<br/>    	var body = response.Content.ReadAsStringAsync();<br/>    	Console.WriteLine(body);<br/>    }';
const baseUrl = "https://messier-api.russiandev.repl.co";
const specialChars = `/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;`;
output.innerHTML = "<pre><code>" + PythonEx + "</code></pre>";
ezCodeOutput.textContent = baseUrl;
/**
 * Removes the hash (#) from the URI when scrolling to an anchor point
 */
function dehash() {
    var uri = window.location.toString();
    var clean_uri = uri.substring(0, uri.indexOf("#"));
    if (uri.indexOf("#") > 0) {
        window.history.replaceState({}, document.title, clean_uri);
    }
}
window.addEventListener("hashchange", (event) => {
    dehash();
});
/*
CODE EXAMPLE BOX
*/
selectElement.addEventListener("change", (event) => {
    // Code box
    if (event.target.value == "Python") {
        output.innerHTML = "<pre><code>" + PythonEx + "</pre></code>";
    }
    else if (event.target.value == "cURL") {
        output.innerHTML = "<pre><code>" + cURLEx + "</pre></code>";
    }
    else if (event.target.value == "Axios") {
        output.innerHTML = "<pre><code>" + AxiosEx + "</pre></code>";
    }
    else if (event.target.value == "HttpClient") {
        output.innerHTML = "<pre><code>" + HttpClientEx + "</pre></code>";
    }
});
/*
LINK GEN
*/
ezCodeElement.addEventListener("change", (event) => {
    // ezCode
    if (event.target.value == "object") {
        var index = prompt("What Messier number?");
        if (index > 110) {
            alert("The index number cannot be greater than 110!");
            ezCodeOutput.textContent = "The index number cannot be greater than 110!";
        }
        else if (index < 1 || index.startsWith("0")) {
            alert("The index number cannot be lower than 1!");
            ezCodeOutput.textContent = "The index number cannot be lower than 1!";
        }
        else if (/[a-z]/i.test(index) == true ||
            specialChars.split("").some((char) => index.includes(char) == true)) {
            alert("The index number can only be an integer!");
            ezCodeOutput.textContent = "The index number can only be an integer!";
        }
        else {
            let format = confirm("Would you like to format?");
            if (format == false) {
                ezCodeOutput.textContent = baseUrl + "?object=" + index;
            }
            else {
                let formatStr = prompt("Available formats:\nxml\nyaml\nhtml\nvisual");
                if (formatStr == "json") {
                    ezCodeOutput.textContent = baseUrl + "?object=" + index;
                }
                else if (formatStr != "xml" &&
                    formatStr != "yaml" &&
                    formatStr != "html" &&
                    formatStr != "visual") {
                    alert("Invalid format type!");
                    ezCodeOutput.textContent = "Invalid format type!";
                }
                else {
                    ezCodeOutput.textContent =
                        baseUrl + "?object=" + index + "&format=" + formatStr;
                }
            }
        }
    }
    else if (event.target.value == "none") {
        ezCodeOutput.textContent = baseUrl;
    }
    else if (event.target.value == "random") {
        let format = confirm("Would you like to format?");
        if (format == false) {
            ezCodeOutput.textContent = baseUrl + "/random";
        }
        else {
            let formatStr = prompt("Available formats:\nxml\nyaml\nhtml\nvisual");
            if (formatStr == "json") {
                ezCodeOutput.textContent = baseUrl + "/random";
            }
            else if (formatStr != "xml" &&
                formatStr != "yaml" &&
                formatStr != "html" &&
                formatStr != "visual") {
                alert("Invalid format type!");
                ezCodeOutput.textContent = "Invalid format type!";
            }
            else {
                ezCodeOutput.textContent = baseUrl + "/random?format=" + formatStr;
            }
        }
    }
    else if (event.target.value == "all") {
        let format = confirm("Would you like to format?");
        if (format == false) {
            ezCodeOutput.textContent = baseUrl + "/all";
        }
        else {
            let formatStr = prompt("Available formats:\nxml\nyaml\nhtml\nvisual");
            if (formatStr == "json") {
                ezCodeOutput.textContent = baseUrl + "/all?format=" + index;
            }
            else if (formatStr != "xml" &&
                formatStr != "yaml" &&
                formatStr != "html" &&
                formatStr != "visual") {
                alert("Invalid format type!");
                ezCodeOutput.textContent = "Invalid format type!";
            }
            else {
                ezCodeOutput.textContent = baseUrl + "/all?format=" + formatStr;
            }
        }
    }
    else if (event.target.value == "convertHashmapJson") {
        let ind = confirm("Click OK to convert JSON -> Hashmap\nClick CANCEL to convert Hashmap -> JSON");
        if (ind == true) {
            let query = prompt("Paste your JSON below:");
            ezCodeOutput.textContent =
                "https://messier-api.russiandev.repl.co/convertHashmapJson?json=" +
                    query;
        }
        else if (ind == false) {
            let query = prompt("Paste your Hashmap below:");
            ezCodeOutput.textContent =
                "https://messier-api.russiandev.repl.co/convertHashmapJson?hashmap=" +
                    query;
        }
    }
});
/*
TYPING EFFECT
*/
// soon™
// make "messier-api" type out && maybe the description underneath
const messierDiv = document.getElementById("messier-api-typeout");
const aboutDiv = document.getElementById("about-typeout");
let text = "";
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
function messierType(str_, ms) {
    return __awaiter(this, void 0, void 0, function* () {
        let length = str_.length;
        console.log({ str_: str_, length: length });
        for (let i = 0; i < length; i++) {
            text = str_[i];
            yield sleep(ms);
            console.log(text);
            messierDiv.insertAdjacentText("beforeend", text);
        }
    });
}
function aboutType(str_, ms) {
    return __awaiter(this, void 0, void 0, function* () {
        let length = str_.length;
        console.log({ "str_": str_, "length": length });
        for (let i = 0; i < length; i++) {
            var text = str_[i];
            yield sleep(ms);
            console.log(text);
            aboutDiv.insertAdjacentText('beforebegin', text);
            aboutDiv.insertAdjacentHTML('beforebegin', '<span id="cursor" class="cursor"> |</span>');
            yield sleep(10);
            const cursorSpan = document.getElementById("cursor");
            console.log("made cursor");
            cursorSpan.remove();
            console.log("removed cursor");
        }
        aboutDiv.insertAdjacentHTML('beforebegin', '<span id="cursor" class="cursor"> |</span>');
    });
}
function runType() {
    return __awaiter(this, void 0, void 0, function* () {
        messierType("messier-api", 50);
        yield sleep(60 * "messier-api".length);
        aboutType("a simple API for getting information on objects in the messier catalog ", 20);
    });
}
runType();
/*
simple API for getting information on objects in the messier catalog
*/
