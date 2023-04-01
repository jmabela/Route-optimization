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

    var cell3 = row.insertCell(2);
    cell3.innerHTML = document.querySelector('#country').value;
 
    var cell4 = row.insertCell(3);
    cell4.innerHTML = document.querySelector('#placeId').value;
    cell4.setAttribute('style','display:none')

    var cell5 = row.insertCell(4);
    cell5.innerHTML = document.querySelector('#cityLat').value;
    cell5.setAttribute('style','display:none')

    var cell6 = row.insertCell(5);
    cell6.innerHTML = document.querySelector('#cityLng').value;
    cell6.setAttribute('style','display:none')
 
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
    var title = document.querySelector('#title').value
    var month = document.querySelector('#month').value
    var year = document.querySelector('#year').value
    console.log(title, month, year)
    var tableBody = document.getElementById("dataTableBody");
    var cityObject = {}
    cityObject['title']=title
    cityObject['month']=month
    cityObject['year']=year
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
            
            url: '/createcity',
           
            data: JSON.stringify(cityObject),
            contentType: "application/json",
            dataType: 'json',
            async: false,
            success: function (result) {
                console.log(result)
                // window.location.href = '/createtrip'

            },
           
        });
    

    
   

    
})
    