const fs = require('fs');

function CreateTable(file) {
    return new Promise((resolve, reject) => {
        let table = [];
        fs.readFile(file, 'utf8', function(ex, content) {
            if(ex) reject(ex);
            else {
                try {
                    var data = content.split('\n');

                    for(let i = 0; i < data.length; i++) {
                        var subData = data[i].split(',');
                        var row = [];

                        for(let j = 0; j < subData.length; j++) {
                            var a = subData[j].replace('\r', '');
                            row.push(a);
                        }
                        table.push(row);
                    }

                    resolve(table);
                } 
                catch (ex) {
                    reject(ex);
                }
            }
        });
    });
};

module.exports = CreateTable;

/*
CreateTable("table.csv").then((table) => {
    console.log(table);
}).catch((error) => {
    console.error(error);
});
*/
