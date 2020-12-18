function setTestCases(){
    var e = document.getElementById("algoOptions");
    var algoSelected = e.options[e.selectedIndex].text;
    document.getElementById('testCases').innerHTML = "";
    var testCase = document.getElementById('testCases');
    // console.log(algoSelected);
    if(algoSelected === "Longest Common Subsequence" || algoSelected === "Shortest Common Supersequence" || algoSelected === "Levenshtein Distance (edit-distance)"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case A' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "Longest Increasing Subsequence" || algoSelected === "Matrix Chain Multiplication (Order finding /paranthesization)" || algoSelected === "Partition-problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case D' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "0-1-knapsack-problem" || algoSelected === "Shortest Common Supersequence"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case F' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "Rod Cutting Problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case H' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "Coin-change-making-problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case I' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "Word Break Problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case J' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }
}

function execute(){
    var e = document.getElementById("algoOptions");
    var algoSelected = e.options[e.selectedIndex].text;

    var t = document.getElementById("testCases");
    var testCaseSelected = t.options[t.selectedIndex].text;

    var inputFile = testCaseSelected + ".txt";

    eel.showInput(inputFile)(function(ret){
        displayInput(ret);
    })

    if(algoSelected === "Longest Common Subsequence"){
        eel.LCS(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Longest Common Subsequence: " + ret ;
        })
    }else if(algoSelected === "Shortest Common Supersequence"){
        eel.SCS(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Shortest Common Supersequence: " + ret ;
        })
    }
}

function displayInput(ret){
    document.getElementById('input').innerHTML = ret;
}