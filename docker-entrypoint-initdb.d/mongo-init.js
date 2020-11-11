ADMIN_USER = "root";
ADMIN_PW = "the_password";
DATABASE = "temp_store";
COLLECTION = "temp";
HOST = "localhost";

let db = connect(HOST + ":27017/" + DATABASE);
db.auth(ADMIN_USER, ADMIN_PW);
let collections = db.getCollectionNames();
let storeFound = false; 
let index;
for(index=0; index<collections.length; index++){
   if (COLLECTION === collections[index]){
       storeFound = true;   
   }
}
if(!storeFound){
   db.createCollection(COLLECTION);
   db.store.createIndex({"temp": 1, "timestamp": 2});

   db.createUser({
    user: 'primary',
    pwd: 'primary',
    roles: [
      {
        role: 'readWrite',
        db: 'temp_store',
      },
    ],
  });
}