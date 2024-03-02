const zod = require("zod");
const emailSchema=zod.string().email();
const passSchema= zod.string().min(8,{message:"Provide minimum 8 characters"});
const userSchema= zod.string();











function signinMiddleWere(req,res,next){
console.log('reached signin');
 const user= req.body;
 if(user.Username||user.Password||user.Useremail){
    try{
    passSchema.parse(user.Password);
    userSchema.parse(user.Username);
    emailSchema.parse(user.Useremail);
   }catch(e){
    console.log(e);
    res.json({
    msg:"input is not valid"
   });
  }
 }
 next();
}

module.exports=signinMiddleWere;
