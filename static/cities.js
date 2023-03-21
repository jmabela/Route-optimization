'use strict';
var citiesList = [];
var placeIdList = []; 


function addRow(tableID) {

    var table = document.getElementById(tableID);
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
 
    var cell1 = row.insertCell(0);
    var element1 = document.createElement("input");
    element1.type = "checkbox";
    element1.name="chkbox[]";
    cell1.appendChild(element1);
 
    var cell2 = row.insertCell(1);
    cell2.innerHTML = document.querySelector('#cityName').value;
    // var element2 = document.createElement("input");
    // element2.type = "text";
    // element2.name = "cityname";
    // element2.value = document.querySelector('#cityName').value
    // cell2.appendChild(element2);
    // citiesList.push(element2.value);
    // console.log(citiesList)

    var cell3 = row.insertCell(2);
    cell3.innerHTML = document.querySelector('#country').value;
    // var element3 = document.createElement("input");
    // element3.type = "text";
    // element3.name = "country";
    // element3.value = document.querySelector('#country').value
    // cell3.appendChild(element3);
    
 
    var cell4 = row.insertCell(3);
    cell4.innerHTML = document.querySelector('#placeId').value;
    // var element4 = document.createElement("input");
    // element4.type = "text";
    // element4.name = "placeid";
    // element4.value = document.querySelector('#placeId').value
    // cell4.appendChild(element4);
    // placeIdList.push(element4.value);
    // console.log(placeIdList)

    var cell5 = row.insertCell(4);
    cell5.innerHTML = document.querySelector('#cityLat').value;
    // var element5 = document.createElement("input");
    // element5.type = "text";
    // element5.name = "citylat";
    // element5.value = document.querySelector('#cityLat').value
    // cell5.appendChild(element5);

    var cell6 = row.insertCell(5);
    cell6.innerHTML = document.querySelector('#cityLng').value;
    // var element6 = document.createElement("input");
    // element6.type = "text";
    // element6.name = "citylng";
    // element6.value = document.querySelector('#cityLng').value
    // cell6.appendChild(element6);
 
   }
 
   function deleteRow(tableID) {
    try {
    var table = document.getElementById(tableID);
    var rowCount = table.rows.length;
 
    for(var i=0; i<rowCount; i++) {
     var row = table.rows[i];
     var chkbox = row.cells[0].childNodes[0];
     if(null != chkbox && true == chkbox.checked) {
      const a = i-1
      table.deleteRow(i);
      rowCount--;
      i--;
     }
 
 
    }
    }catch(e) {
     alert(e);
    }
   }




const createTripButton = document.querySelector('#addCities');

createTripButton.addEventListener('click', (evt)=> {
    // evt.preventDefault();
    var tableBody = document.getElementById("dataTableBody");
    var cityObject = {}
    for (var i = 1, row; row = tableBody.rows[i]; i++) {
        //iterate through rows
        
        let city =row.cells[1].innerHTML;
        let country=row.cells[2].innerHTML;
        let placeId=row.cells[3].innerHTML;
        let cityLat=row.cells[4].innerHTML;
        let cityLng=row.cells[5].innerHTML;
        
        var row_object = {
            "city" : city,
            "country": country,
            "placeId": placeId,
            "cityLat": cityLat,
            "cityLng": cityLng
        }
        
        cityObject[i] = row_object; 

    }
        $.ajax({
            type: 'POST',
            // url: "{{url_for('/createtrip')}}",
            url: '/createcity',
            // contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify(cityObject),
            contentType: "application/json",
            dataType: 'json',
            async: false,
            success: function (result) {
                console.log(result)

            },
            // error: function(xhr, status, error) {
            //     console.log(status);
            //     console.log(error);
            // },
            // instead of a post do get 
        });
    

    
   

    
})
    