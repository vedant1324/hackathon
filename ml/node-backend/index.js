const express = require ("express");
const mongoose = require("mongoose");
const signinMiddleWere = require("./middlewere/signin");
const loginMiddleWere = require("./middlewere/login");
require('dotenv').config();
const app=express();
app.use(express.json());


mongoose.connect(process.env.MONGO_CONNECT_LINK);
const loginSchema=mongoose.Schema({
  Useremail:String,
  UserName:String,
  PassWord:String,

});
const loginModel=mongoose.model("Users",loginSchema);
app.post("/signin",signinMiddleWere,async (req,res)=>{
    const Useremail=req.body.Useremail;
    const Username=req.body.Username;
    const Password=req.body.Password;

    const userLogin= new loginModel({
    Useremail:Useremail,
    UserName:Username,
    PassWord:Password,
    });
    await userLogin.save()
        res.json({
            msg: "user created"
        });
    
});
app.post("/login",loginMiddleWere,async (req,res)=>{
    const Username=req.body.Username;
    const Password=req.body.Password;

    const user=await loginModel.findOne({
    UserName:Username,
    PassWord:Password,
    });
    console.log(user);
    if(!user){
        res.status(400).json({
            msg:"invalid",
        });
        return;
    }
   
    res.status(200).json({
        msg:"user exists",
    }) 
});

app.listen(3000);
