const zod = require("zod");


const passSchema= zod.string().min(8,{message:"Provide minimum 8 characters"});
const userSchema= zod.string();


function loginMiddleWere(req,res,next){
console.log('reached login');
 const user= req.body;
 if(user.Username||user.Password||user.Useremail){
    try{
    passSchema.parse(user.Password);
    userSchema.parse(user.Username);
   }catch(e){
    console.log(e);
    res.json({
    msg:"input is not valid"
   });
  }
 }
 next();
}

module.exports=loginMiddleWere;