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
    }else if(algoSelected === "Rod Cutting Problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case H' + i);
            newTestCase.appendChild(newTestCaseText);
            testCase.appendChild(newTestCase);
            // console.log(testCase);
        }  
    }else if(algoSelected === "0-1-knapsack-problem"){
        for(i = 1; i <= 10; i++){
            var newTestCase = document.createElement('option');
            var newTestCaseText = document.createTextNode('Test Case F' + i);
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
            document.getElementById('output').innerHTML = "Longest Common Subsequence: " + ret.join("") + "\nLength: " + (ret.length-1);
        })
    }else if(algoSelected === "Shortest Common Supersequence"){
        eel.SCS(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Shortest Common Supersequence: " + ret + "Length: " + (ret.length-1);
        })
    }else if(algoSelected === "Levenshtein Distance (edit-distance)"){
        eel.editDistance(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Levenshtein Distance (edit-distance) value: " + ret ;
        })
    }else if(algoSelected === "Longest Increasing Subsequence"){
        eel.LIS(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Longest Increasing Subsequence: " + ret + "\nLength: " + ret.length;
        })
    }else if(algoSelected === "Matrix Chain Multiplication (Order finding /paranthesization)"){
        eel.matrixChain(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Matrix Chain Multiplication (Order finding/paranthesization) =>\nMinimum/Optimal number of multiplications needed: " + ret ;
        })
    }else if(algoSelected === "Partition-problem"){
        eel.Partition(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Partition-problem (True (Possible)/False (Not-Possible)): " + ret.toString().charAt(0).toUpperCase() + ret.toString().slice(1);
        })
    }else if(algoSelected === "0-1-knapsack-problem"){
        eel.Knapsack(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Solution to 0-1-knapsack-problem =>" + "\nMaximum value obtained from 'n' items: " + ret ;
        })
    }else if(algoSelected === "Rod Cutting Problem"){
        eel.rodcutting(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Rod Cutting Problem =>" + "\nNumber of required pieces/cuts): " + ret ;
        })
    }else if(algoSelected === "Coin-change-making-problem"){
        eel.coinChange(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Coin-change-making-problem=>" + "\nTotal number of combinations of the coins which can be arranged: " + ret ;
        })
    }else if(algoSelected === "Word Break Problem"){
        eel.Word_Break(inputFile)(function(ret){
            document.getElementById('output').innerHTML = "Solution to Word Break Problem: " + ret ;
        })
    }
}

function displayInput(ret){
    document.getElementById('input').innerHTML = ret;
}