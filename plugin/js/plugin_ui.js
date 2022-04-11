var background = chrome.extension.getBackgroundPage();
var colors = {
    "-1": "#00A82D",
    "0": "#FFF",
    "1": "#F7164F"
};
var featureList = document.getElementById("features");

var result;
chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    var _this = this;
    _this.result = background.results[tabs[0].id];
    var isPhish = background.isPhish[tabs[0].id];
    var legitimatePercent = background.legitimatePercents[tabs[0].id];

    if (legitimatePercent == undefined) {
        $("#refresh_msg").text("Please Refresh Current Page");
        return;
    }

    $("#refresh_msg").text("");

    $("#site_score").text("SAFE");
    $("#site_score").css("color", "#00A82D");
    $("#site_percent").text(parseInt(legitimatePercent) + "%");
    $("#site_percent").css("color", "#00A82D");
    $("#site_msg1").text("This website is safe to use.");
    $("#site_msg1").css("color", "#00A82D");
    if (isPhish) {
        $("#site_score").text("PHISHING");
        $("#site_score").css("color", "#F7164F");
        $("#site_percent").text(parseInt(legitimatePercent) - 20 + "%");
        $("#site_percent").css("color", "#F7164F");
        $("#site_msg1").text("Warning!! You're being phished.");
        $("#site_msg1").css("color", "#F7164F");

    }
});

$("#detail_btn").bind("click", function () {
    var text = $("#detail_btn")[0].innerText
    console.log(text)
    if (text == "Show details") {
        $("#detail_btn").text("Hide details");
        for (var key in result) {
            var newFeature = document.createElement("li");
            newFeature.textContent = key;
            newFeature.style.color = colors[result[key]];
            featureList.appendChild(newFeature);
        }
    } else {
        $("#features").empty();
        $("#detail_btn").text("Show details");
    }
});

jQuery(document).ready(function ($) {
    $("#inner-content").slimScroll({
        height: '470px'
    });
});

