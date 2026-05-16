# # # # # import streamlit as st
# # # # # import streamlit.components.v1 as components

# # # # # st.set_page_config(
# # # # #     page_title="Hidden Lamp Login",
# # # # #     layout="centered"
# # # # # )

# # # # # html_code = """
# # # # # <!DOCTYPE html>
# # # # # <html>
# # # # # <head>

# # # # # <style>

# # # # # body{
# # # # #     margin:0;
# # # # #     padding:0;
# # # # #     background:#0d0d0d;
# # # # #     overflow:hidden;
# # # # #     font-family:Arial, sans-serif;
# # # # # }

# # # # # /* Main Container */

# # # # # .container{
# # # # #     display:flex;
# # # # #     flex-direction:column;
# # # # #     align-items:center;
# # # # #     justify-content:flex-start;
# # # # #     height:100vh;
# # # # #     padding-top:20px;
# # # # # }

# # # # # /* Ceiling */

# # # # # .ceiling{
# # # # #     width:100%;
# # # # #     height:20px;
# # # # #     background:#1f1f1f;
# # # # #     position:absolute;
# # # # #     top:0;
# # # # # }

# # # # # /* Wire */

# # # # # .wire{
# # # # #     width:4px;
# # # # #     height:240px;
# # # # #     background:white;
# # # # #     position:relative;
# # # # #     cursor:pointer;
# # # # # }

# # # # # /* Pull Knob */

# # # # # .knob{
# # # # #     width:22px;
# # # # #     height:22px;
# # # # #     border-radius:50%;
# # # # #     background:#f2f2f2;
# # # # #     position:absolute;
# # # # #     bottom:-10px;
# # # # #     left:50%;
# # # # #     transform:translateX(-50%);
# # # # #     box-shadow:0 0 10px rgba(255,255,255,0.5);
# # # # # }

# # # # # /* Lamp */

# # # # # .lamp{
# # # # #     width:160px;
# # # # #     height:80px;
# # # # #     background:linear-gradient(to bottom,#555,#111);
# # # # #     border-radius:0 0 80px 80px;
# # # # #     margin-top:-2px;
# # # # #     position:relative;
# # # # #     transition:0.5s;
# # # # # }

# # # # # /* Lamp ON */

# # # # # .lamp.on{
# # # # #     background:linear-gradient(to bottom,#ffe680,#d4a900);
# # # # #     box-shadow:0 0 40px rgba(255,255,180,0.9);
# # # # # }

# # # # # /* Light Glow */

# # # # # .glow{
# # # # #     width:320px;
# # # # #     height:320px;
# # # # #     background:radial-gradient(circle,
# # # # #     rgba(255,255,180,0.55) 0%,
# # # # #     rgba(255,255,180,0.2) 35%,
# # # # #     transparent 70%);
# # # # #     position:absolute;
# # # # #     top:70px;
# # # # #     left:50%;
# # # # #     transform:translateX(-50%);
# # # # #     opacity:0;
# # # # #     transition:0.7s;
# # # # # }

# # # # # /* Glow Visible */

# # # # # .glow.show{
# # # # #     opacity:1;
# # # # # }

# # # # # /* Login Box */

# # # # # .login-box{
# # # # #     width:340px;
# # # # #     background:#161616;
# # # # #     padding:30px;
# # # # #     border-radius:20px;
# # # # #     margin-top:60px;
# # # # #     opacity:0;
# # # # #     transform:translateY(80px);
# # # # #     transition:0.8s;
# # # # #     box-shadow:0 0 25px rgba(255,255,255,0.08);
# # # # # }

# # # # # /* Show Login */

# # # # # .login-box.show{
# # # # #     opacity:1;
# # # # #     transform:translateY(0);
# # # # # }

# # # # # /* Title */

# # # # # .title{
# # # # #     text-align:center;
# # # # #     color:white;
# # # # #     font-size:28px;
# # # # #     margin-bottom:20px;
# # # # #     font-weight:bold;
# # # # # }

# # # # # /* Inputs */

# # # # # input{
# # # # #     width:100%;
# # # # #     padding:14px;
# # # # #     margin-top:15px;
# # # # #     border:none;
# # # # #     border-radius:10px;
# # # # #     background:#262626;
# # # # #     color:white;
# # # # #     font-size:16px;
# # # # # }

# # # # # /* Button */

# # # # # button{
# # # # #     width:100%;
# # # # #     padding:14px;
# # # # #     margin-top:20px;
# # # # #     border:none;
# # # # #     border-radius:10px;
# # # # #     background:#f7c948;
# # # # #     color:black;
# # # # #     font-size:18px;
# # # # #     font-weight:bold;
# # # # #     cursor:pointer;
# # # # #     transition:0.3s;
# # # # # }

# # # # # button:hover{
# # # # #     transform:scale(1.03);
# # # # # }

# # # # # /* Message */

# # # # # .message{
# # # # #     margin-top:15px;
# # # # #     text-align:center;
# # # # #     font-size:15px;
# # # # # }

# # # # # /* Responsive */

# # # # # @media(max-width:500px){

# # # # #     .lamp{
# # # # #         width:120px;
# # # # #         height:60px;
# # # # #     }

# # # # #     .wire{
# # # # #         height:200px;
# # # # #     }

# # # # #     .login-box{
# # # # #         width:90%;
# # # # #     }

# # # # #     .glow{
# # # # #         width:240px;
# # # # #         height:240px;
# # # # #     }
# # # # # }

# # # # # </style>

# # # # # </head>

# # # # # <body>

# # # # # <div class="ceiling"></div>

# # # # # <div class="container">

# # # # #     <!-- Wire -->
# # # # #     <div class="wire" id="wire">
# # # # #         <div class="knob"></div>
# # # # #     </div>

# # # # #     <!-- Lamp -->
# # # # #     <div class="lamp" id="lamp">
# # # # #         <div class="glow" id="glow"></div>
# # # # #     </div>

# # # # #     <!-- Login Box -->
# # # # #     <div class="login-box" id="loginBox">

# # # # #         <div class="title">Login</div>

# # # # #         <input type="text" id="username" placeholder="Username">

# # # # #         <input type="password" id="password" placeholder="Password">

# # # # #         <button onclick="login()">Login</button>

# # # # #         <div class="message" id="message"></div>

# # # # #     </div>

# # # # # </div>

# # # # # <script>

# # # # # let active = false;

# # # # # document.getElementById("wire").addEventListener("click", function(){

# # # # #     const lamp = document.getElementById("lamp");
# # # # #     const glow = document.getElementById("glow");
# # # # #     const loginBox = document.getElementById("loginBox");

# # # # #     active = !active;

# # # # #     if(active){

# # # # #         lamp.classList.add("on");
# # # # #         glow.classList.add("show");
# # # # #         loginBox.classList.add("show");

# # # # #     }else{

# # # # #         lamp.classList.remove("on");
# # # # #         glow.classList.remove("show");
# # # # #         loginBox.classList.remove("show");
# # # # #     }
# # # # # });

# # # # # function login(){

# # # # #     const username = document.getElementById("username").value;
# # # # #     const password = document.getElementById("password").value;

# # # # #     const message = document.getElementById("message");

# # # # #     if(username === "admin" && password === "1234"){

# # # # #         message.style.color = "#00ff99";
# # # # #         message.innerHTML = "Login Successful";

# # # # #     }else{

# # # # #         message.style.color = "#ff4d4d";
# # # # #         message.innerHTML = "Invalid Username or Password";
# # # # #     }
# # # # # }

# # # # # </script>

# # # # # </body>
# # # # # </html>
# # # # # """

# # # # # components.html(html_code, height=950)





# # # # import streamlit as st
# # # # import streamlit.components.v1 as components

# # # # st.set_page_config(
# # # #     page_title="Lamp Secret Game",
# # # #     layout="centered"
# # # # )

# # # # html_code = """
# # # # <!DOCTYPE html>
# # # # <html>
# # # # <head>

# # # # <style>

# # # # body{
# # # #     margin:0;
# # # #     padding:0;
# # # #     background:#0d0d0d;
# # # #     overflow:hidden;
# # # #     font-family:Arial, sans-serif;
# # # # }

# # # # /* Main Container */

# # # # .container{
# # # #     display:flex;
# # # #     flex-direction:column;
# # # #     align-items:center;
# # # #     justify-content:flex-start;
# # # #     height:100vh;
# # # #     padding-top:20px;
# # # # }

# # # # /* Ceiling */

# # # # .ceiling{
# # # #     width:100%;
# # # #     height:20px;
# # # #     background:#1c1c1c;
# # # #     position:absolute;
# # # #     top:0;
# # # # }

# # # # /* Wire */

# # # # .wire{
# # # #     width:4px;
# # # #     height:240px;
# # # #     background:white;
# # # #     position:relative;
# # # #     cursor:pointer;
# # # # }

# # # # /* Pull Ball */

# # # # .knob{
# # # #     width:22px;
# # # #     height:22px;
# # # #     border-radius:50%;
# # # #     background:#f1f1f1;
# # # #     position:absolute;
# # # #     bottom:-10px;
# # # #     left:50%;
# # # #     transform:translateX(-50%);
# # # #     box-shadow:0 0 10px rgba(255,255,255,0.5);
# # # # }

# # # # /* Lamp */

# # # # .lamp{
# # # #     width:170px;
# # # #     height:85px;
# # # #     background:linear-gradient(to bottom,#555,#111);
# # # #     border-radius:0 0 90px 90px;
# # # #     position:relative;
# # # #     margin-top:-2px;
# # # #     transition:0.5s;
# # # # }

# # # # /* Lamp ON */

# # # # .lamp.on{
# # # #     background:linear-gradient(to bottom,#ffe680,#c79a00);
# # # #     box-shadow:0 0 45px rgba(255,255,180,0.9);
# # # # }

# # # # /* Glow */

# # # # .glow{
# # # #     width:340px;
# # # #     height:340px;
# # # #     background:radial-gradient(circle,
# # # #     rgba(255,255,180,0.6) 0%,
# # # #     rgba(255,255,180,0.2) 35%,
# # # #     transparent 70%);
# # # #     position:absolute;
# # # #     top:75px;
# # # #     left:50%;
# # # #     transform:translateX(-50%);
# # # #     opacity:0;
# # # #     transition:0.8s;
# # # # }

# # # # .glow.show{
# # # #     opacity:1;
# # # # }

# # # # /* Login Box */

# # # # .login-box{
# # # #     width:340px;
# # # #     background:#151515;
# # # #     padding:30px;
# # # #     border-radius:20px;
# # # #     margin-top:60px;
# # # #     opacity:0;
# # # #     transform:translateY(80px);
# # # #     transition:0.8s;
# # # #     box-shadow:0 0 25px rgba(255,255,255,0.08);
# # # # }

# # # # /* Show Login */

# # # # .login-box.show{
# # # #     opacity:1;
# # # #     transform:translateY(0);
# # # # }

# # # # /* Title */

# # # # .title{
# # # #     text-align:center;
# # # #     color:white;
# # # #     font-size:30px;
# # # #     margin-bottom:20px;
# # # #     font-weight:bold;
# # # # }

# # # # /* Inputs */

# # # # input{
# # # #     width:100%;
# # # #     padding:14px;
# # # #     margin-top:15px;
# # # #     border:none;
# # # #     border-radius:10px;
# # # #     background:#262626;
# # # #     color:white;
# # # #     font-size:16px;
# # # # }

# # # # /* Button */

# # # # button{
# # # #     width:100%;
# # # #     padding:14px;
# # # #     margin-top:20px;
# # # #     border:none;
# # # #     border-radius:10px;
# # # #     background:#f7c948;
# # # #     color:black;
# # # #     font-size:18px;
# # # #     font-weight:bold;
# # # #     cursor:pointer;
# # # #     transition:0.3s;
# # # # }

# # # # button:hover{
# # # #     transform:scale(1.03);
# # # # }

# # # # /* Message */

# # # # .message{
# # # #     margin-top:15px;
# # # #     text-align:center;
# # # #     font-size:15px;
# # # # }

# # # # /* Game Box */

# # # # .game-box{
# # # #     display:none;
# # # #     margin-top:50px;
# # # #     text-align:center;
# # # #     color:white;
# # # # }

# # # # /* Game Button */

# # # # .game-btn{
# # # #     width:180px;
# # # #     margin-top:25px;
# # # # }

# # # # /* Score */

# # # # .score{
# # # #     margin-top:20px;
# # # #     font-size:26px;
# # # #     color:#ffe680;
# # # # }

# # # # /* Responsive */

# # # # @media(max-width:500px){

# # # #     .lamp{
# # # #         width:120px;
# # # #         height:60px;
# # # #     }

# # # #     .wire{
# # # #         height:200px;
# # # #     }

# # # #     .login-box{
# # # #         width:90%;
# # # #     }

# # # #     .glow{
# # # #         width:240px;
# # # #         height:240px;
# # # #     }
# # # # }

# # # # </style>

# # # # </head>

# # # # <body>

# # # # <div class="ceiling"></div>

# # # # <div class="container">

# # # #     <!-- Wire -->
# # # #     <div class="wire" id="wire">
# # # #         <div class="knob"></div>
# # # #     </div>

# # # #     <!-- Lamp -->
# # # #     <div class="lamp" id="lamp">
# # # #         <div class="glow" id="glow"></div>
# # # #     </div>

# # # #     <!-- Login -->
# # # #     <div class="login-box" id="loginBox">

# # # #         <div class="title">Login</div>

# # # #         <input type="text" id="username" placeholder="Username">

# # # #         <input type="password" id="password" placeholder="Password">

# # # #         <button onclick="login()">Login</button>

# # # #         <div class="message" id="message"></div>

# # # #     </div>

# # # #     <!-- Secret Game -->
# # # #     <div class="game-box" id="gameBox">

# # # #         <h1>Secret Click Game</h1>

# # # #         <p>Click the button and increase your score.</p>

# # # #         <button class="game-btn" onclick="increaseScore()">
# # # #             Click Me
# # # #         </button>

# # # #         <div class="score" id="score">
# # # #             Score : 0
# # # #         </div>

# # # #     </div>

# # # # </div>

# # # # <script>

# # # # let active = false;
# # # # let score = 0;

# # # # /* Pull Wire */

# # # # document.getElementById("wire").addEventListener("click", function(){

# # # #     const lamp = document.getElementById("lamp");
# # # #     const glow = document.getElementById("glow");
# # # #     const loginBox = document.getElementById("loginBox");

# # # #     active = !active;

# # # #     if(active){

# # # #         lamp.classList.add("on");
# # # #         glow.classList.add("show");
# # # #         loginBox.classList.add("show");

# # # #     }else{

# # # #         lamp.classList.remove("on");
# # # #         glow.classList.remove("show");
# # # #         loginBox.classList.remove("show");
# # # #     }
# # # # });

# # # # /* Login */

# # # # function login(){

# # # #     const username = document.getElementById("username").value;
# # # #     const password = document.getElementById("password").value;

# # # #     const message = document.getElementById("message");

# # # #     if(username === "advait" && password === "12345"){

# # # #         document.getElementById("loginBox").style.display = "none";

# # # #         document.getElementById("gameBox").style.display = "block";

# # # #     }else{

# # # #         message.style.color = "#ff4d4d";
# # # #         message.innerHTML = "Invalid Username or Password";
# # # #     }
# # # # }

# # # # /* Game */

# # # # function increaseScore(){

# # # #     score++;

# # # #     document.getElementById("score").innerHTML =
# # # #         "Score : " + score;
# # # # }

# # # # </script>

# # # # </body>
# # # # </html>
# # # # """

# # # # components.html(html_code, height=1000)







# # # import streamlit as st
# # # import streamlit.components.v1 as components

# # # st.set_page_config(
# # #     page_title="Lamp TikTok Game",
# # #     layout="centered"
# # # )

# # # html_code = """
# # # <!DOCTYPE html>
# # # <html>
# # # <head>

# # # <style>

# # # body{
# # #     margin:0;
# # #     padding:0;
# # #     background:#0c0c0c;
# # #     overflow:hidden;
# # #     font-family:Arial, sans-serif;
# # # }

# # # /* Main */

# # # .container{
# # #     display:flex;
# # #     flex-direction:column;
# # #     align-items:center;
# # #     height:100vh;
# # #     padding-top:20px;
# # # }

# # # /* Ceiling */

# # # .ceiling{
# # #     width:100%;
# # #     height:20px;
# # #     background:#1a1a1a;
# # #     position:absolute;
# # #     top:0;
# # # }

# # # /* Wire */

# # # .wire{
# # #     width:4px;
# # #     height:230px;
# # #     background:white;
# # #     position:relative;
# # #     cursor:pointer;
# # # }

# # # /* Knob */

# # # .knob{
# # #     width:22px;
# # #     height:22px;
# # #     border-radius:50%;
# # #     background:white;
# # #     position:absolute;
# # #     bottom:-10px;
# # #     left:50%;
# # #     transform:translateX(-50%);
# # # }

# # # /* Lamp */

# # # .lamp{
# # #     width:170px;
# # #     height:85px;
# # #     background:linear-gradient(to bottom,#555,#111);
# # #     border-radius:0 0 90px 90px;
# # #     margin-top:-2px;
# # #     transition:0.5s;
# # #     position:relative;
# # # }

# # # /* Lamp ON */

# # # .lamp.on{
# # #     background:linear-gradient(to bottom,#ffe680,#c89d00);
# # #     box-shadow:0 0 45px rgba(255,255,180,0.9);
# # # }

# # # /* Glow */

# # # .glow{
# # #     width:340px;
# # #     height:340px;
# # #     background:radial-gradient(circle,
# # #     rgba(255,255,180,0.55) 0%,
# # #     rgba(255,255,180,0.18) 35%,
# # #     transparent 70%);
# # #     position:absolute;
# # #     top:70px;
# # #     left:50%;
# # #     transform:translateX(-50%);
# # #     opacity:0;
# # #     transition:0.8s;
# # # }

# # # .glow.show{
# # #     opacity:1;
# # # }

# # # /* Login */

# # # .login-box{
# # #     width:340px;
# # #     background:#161616;
# # #     padding:30px;
# # #     border-radius:20px;
# # #     margin-top:60px;
# # #     opacity:0;
# # #     transform:translateY(80px);
# # #     transition:0.8s;
# # #     box-shadow:0 0 20px rgba(255,255,255,0.08);
# # # }

# # # .login-box.show{
# # #     opacity:1;
# # #     transform:translateY(0);
# # # }

# # # /* Title */

# # # .title{
# # #     color:white;
# # #     text-align:center;
# # #     font-size:30px;
# # #     margin-bottom:20px;
# # # }

# # # /* Inputs */

# # # input{
# # #     width:100%;
# # #     padding:14px;
# # #     margin-top:15px;
# # #     border:none;
# # #     border-radius:10px;
# # #     background:#252525;
# # #     color:white;
# # #     font-size:16px;
# # # }

# # # /* Buttons */

# # # button{
# # #     width:100%;
# # #     padding:14px;
# # #     margin-top:20px;
# # #     border:none;
# # #     border-radius:10px;
# # #     background:#f7c948;
# # #     color:black;
# # #     font-size:18px;
# # #     font-weight:bold;
# # #     cursor:pointer;
# # # }

# # # /* Error */

# # # .message{
# # #     text-align:center;
# # #     margin-top:15px;
# # #     color:#ff4d4d;
# # # }

# # # /* TikTok Game */

# # # .game{
# # #     display:none;
# # #     margin-top:40px;
# # #     text-align:center;
# # #     color:white;
# # # }

# # # /* Game Grid */

# # # .grid{
# # #     display:grid;
# # #     grid-template-columns:repeat(3,100px);
# # #     gap:10px;
# # #     margin-top:20px;
# # # }

# # # /* Box */

# # # .box{
# # #     width:100px;
# # #     height:100px;
# # #     background:#1f1f1f;
# # #     border-radius:15px;
# # #     display:flex;
# # #     align-items:center;
# # #     justify-content:center;
# # #     font-size:40px;
# # #     cursor:pointer;
# # #     transition:0.2s;
# # # }

# # # .box:hover{
# # #     transform:scale(1.05);
# # # }

# # # /* Score */

# # # .score{
# # #     margin-top:20px;
# # #     font-size:24px;
# # #     color:#ffe680;
# # # }

# # # </style>

# # # </head>

# # # <body>

# # # <div class="ceiling"></div>

# # # <div class="container">

# # #     <!-- Wire -->
# # #     <div class="wire" id="wire">
# # #         <div class="knob"></div>
# # #     </div>

# # #     <!-- Lamp -->
# # #     <div class="lamp" id="lamp">
# # #         <div class="glow" id="glow"></div>
# # #     </div>

# # #     <!-- Login -->
# # #     <div class="login-box" id="loginBox">

# # #         <div class="title">Login</div>

# # #         <input type="text" id="username" placeholder="Username">

# # #         <input type="password" id="password" placeholder="Password">

# # #         <button onclick="login()">Login</button>

# # #         <div class="message" id="message"></div>

# # #     </div>

# # #     <!-- TikTok Game -->
# # #     <div class="game" id="game">

# # #         <h1>Tik Tok Game</h1>

# # #         <p>Catch the TikTok icons before they disappear.</p>

# # #         <div class="grid">

# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>

# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>

# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>
# # #             <div class="box" onclick="catchTikTok(this)"></div>

# # #         </div>

# # #         <div class="score" id="score">
# # #             Score : 0
# # #         </div>

# # #     </div>

# # # </div>

# # # <script>

# # # let active = false;
# # # let score = 0;
# # # let currentBox = null;

# # # /* Pull Wire */

# # # document.getElementById("wire").addEventListener("click", function(){

# # #     const lamp = document.getElementById("lamp");
# # #     const glow = document.getElementById("glow");
# # #     const loginBox = document.getElementById("loginBox");

# # #     active = !active;

# # #     if(active){

# # #         lamp.classList.add("on");
# # #         glow.classList.add("show");
# # #         loginBox.classList.add("show");

# # #     }else{

# # #         lamp.classList.remove("on");
# # #         glow.classList.remove("show");
# # #         loginBox.classList.remove("show");
# # #     }
# # # });

# # # /* Login */

# # # function login(){

# # #     const username =
# # #         document.getElementById("username").value;

# # #     const password =
# # #         document.getElementById("password").value;

# # #     if(username === "advait" &&
# # #        password === "12345"){

# # #         document.getElementById("loginBox")
# # #             .style.display = "none";

# # #         document.getElementById("game")
# # #             .style.display = "block";

# # #         startGame();

# # #     }else{

# # #         document.getElementById("message")
# # #             .innerHTML =
# # #             "Invalid Username or Password";
# # #     }
# # # }

# # # /* TikTok Game */

# # # function startGame(){

# # #     const boxes =
# # #         document.querySelectorAll(".box");

# # #     setInterval(() => {

# # #         boxes.forEach(box => {
# # #             box.innerHTML = "";
# # #         });

# # #         let random =
# # #             Math.floor(Math.random() * boxes.length);

# # #         currentBox = boxes[random];

# # #         currentBox.innerHTML = "🎵";

# # #     }, 800);
# # # }

# # # /* Catch */

# # # function catchTikTok(box){

# # #     if(box === currentBox &&
# # #        box.innerHTML === "🎵"){

# # #         score++;

# # #         document.getElementById("score")
# # #             .innerHTML =
# # #             "Score : " + score;

# # #         box.innerHTML = "";
# # #     }
# # # }

# # # </script>

# # # </body>

# # # </html>
# # # """

# # # components.html(html_code, height=1200)





# # import streamlit as st
# # import streamlit.components.v1 as components

# # st.set_page_config(
# #     page_title="Lamp Tic Tac Toe",
# #     layout="centered"
# # )

# # html_code = """
# # <!DOCTYPE html>
# # <html>
# # <head>

# # <style>

# # body{
# #     margin:0;
# #     padding:0;
# #     background:#0a0a0a;
# #     overflow:hidden;
# #     font-family:Arial, sans-serif;
# #     color:white;
# # }

# # /* Main */

# # .container{
# #     display:flex;
# #     flex-direction:column;
# #     align-items:center;
# #     min-height:100vh;
# #     padding-top:20px;
# # }

# # /* Ceiling */

# # .ceiling{
# #     width:100%;
# #     height:18px;
# #     background:#151515;
# #     position:absolute;
# #     top:0;
# # }

# # /* Wire */

# # .wire{
# #     width:4px;
# #     height:240px;
# #     background:white;
# #     position:relative;
# #     cursor:pointer;
# # }

# # /* Pull Knob */

# # .knob{
# #     width:24px;
# #     height:24px;
# #     border-radius:50%;
# #     background:white;
# #     position:absolute;
# #     bottom:-10px;
# #     left:50%;
# #     transform:translateX(-50%);
# # }

# # /* Lamp */

# # .lamp{
# #     width:180px;
# #     height:90px;
# #     background:linear-gradient(to bottom,#555,#111);
# #     border-radius:0 0 90px 90px;
# #     margin-top:-2px;
# #     position:relative;
# #     transition:0.5s;
# # }

# # /* Lamp ON */

# # .lamp.on{
# #     background:linear-gradient(to bottom,#ffe680,#d8a600);
# #     box-shadow:0 0 45px rgba(255,255,180,0.9);
# # }

# # /* Glow */

# # .glow{
# #     width:360px;
# #     height:360px;
# #     background:radial-gradient(circle,
# #     rgba(255,240,180,0.55) 0%,
# #     rgba(255,240,180,0.18) 35%,
# #     transparent 70%);
# #     position:absolute;
# #     top:70px;
# #     left:50%;
# #     transform:translateX(-50%);
# #     opacity:0;
# #     transition:0.8s;
# # }

# # .glow.show{
# #     opacity:1;
# # }

# # /* Login Box */

# # .login-box{
# #     width:360px;
# #     background:#151515;
# #     padding:30px;
# #     border-radius:25px;
# #     margin-top:60px;
# #     opacity:0;
# #     transform:translateY(80px);
# #     transition:0.8s;
# #     box-shadow:0 0 30px rgba(255,255,255,0.08);
# # }

# # .login-box.show{
# #     opacity:1;
# #     transform:translateY(0);
# # }

# # /* Title */

# # .title{
# #     text-align:center;
# #     font-size:34px;
# #     margin-bottom:25px;
# # }

# # /* Inputs */

# # input{
# #     width:100%;
# #     padding:15px;
# #     margin-top:15px;
# #     border:none;
# #     border-radius:12px;
# #     background:#232323;
# #     color:white;
# #     font-size:16px;
# # }

# # /* Button */

# # button{
# #     width:100%;
# #     padding:15px;
# #     margin-top:20px;
# #     border:none;
# #     border-radius:12px;
# #     background:#f7c948;
# #     color:black;
# #     font-size:18px;
# #     font-weight:bold;
# #     cursor:pointer;
# # }

# # /* Message */

# # .message{
# #     text-align:center;
# #     margin-top:15px;
# #     color:#ff4d4d;
# # }

# # /* Game */

# # .game{
# #     display:none;
# #     margin-top:40px;
# #     text-align:center;
# # }

# # /* Tic Tac Toe Grid */

# # .board{
# #     display:grid;
# #     grid-template-columns:repeat(3,100px);
# #     gap:10px;
# #     margin-top:25px;
# # }

# # /* Cell */

# # .cell{
# #     width:100px;
# #     height:100px;
# #     background:#181818;
# #     border-radius:15px;
# #     display:flex;
# #     align-items:center;
# #     justify-content:center;
# #     font-size:45px;
# #     cursor:pointer;
# #     transition:0.2s;
# # }

# # .cell:hover{
# #     transform:scale(1.05);
# #     background:#242424;
# # }

# # /* Status */

# # .status{
# #     margin-top:25px;
# #     font-size:28px;
# #     color:#ffe680;
# # }

# # /* Restart */

# # .restart{
# #     width:220px;
# #     margin-top:25px;
# # }

# # </style>

# # </head>

# # <body>

# # <div class="ceiling"></div>

# # <div class="container">

# #     <!-- Wire -->
# #     <div class="wire" id="wire">
# #         <div class="knob"></div>
# #     </div>

# #     <!-- Lamp -->
# #     <div class="lamp" id="lamp">
# #         <div class="glow" id="glow"></div>
# #     </div>

# #     <!-- Login -->
# #     <div class="login-box" id="loginBox">

# #         <div class="title">Login</div>

# #         <input type="text"
# #         id="username"
# #         placeholder="Username">

# #         <input type="password"
# #         id="password"
# #         placeholder="Password">

# #         <button onclick="login()">
# #             Login
# #         </button>

# #         <div class="message"
# #         id="message"></div>

# #     </div>

# #     <!-- Game -->

# #     <div class="game" id="game">

# #         <h1>Tic Tac Toe</h1>

# #         <div class="board">

# #             <div class="cell" onclick="play(this,0)"></div>
# #             <div class="cell" onclick="play(this,1)"></div>
# #             <div class="cell" onclick="play(this,2)"></div>

# #             <div class="cell" onclick="play(this,3)"></div>
# #             <div class="cell" onclick="play(this,4)"></div>
# #             <div class="cell" onclick="play(this,5)"></div>

# #             <div class="cell" onclick="play(this,6)"></div>
# #             <div class="cell" onclick="play(this,7)"></div>
# #             <div class="cell" onclick="play(this,8)"></div>

# #         </div>

# #         <div class="status" id="status">
# #             Player X Turn
# #         </div>

# #         <button class="restart"
# #         onclick="restartGame()">
# #             Restart Game
# #         </button>

# #     </div>

# # </div>

# # <script>

# # let active = false;

# # /* Lamp */

# # document.getElementById("wire")
# # .addEventListener("click", function(){

# #     const lamp =
# #     document.getElementById("lamp");

# #     const glow =
# #     document.getElementById("glow");

# #     const loginBox =
# #     document.getElementById("loginBox");

# #     active = !active;

# #     if(active){

# #         lamp.classList.add("on");
# #         glow.classList.add("show");
# #         loginBox.classList.add("show");

# #     }else{

# #         lamp.classList.remove("on");
# #         glow.classList.remove("show");
# #         loginBox.classList.remove("show");
# #     }
# # });

# # /* Login */

# # function login(){

# #     const username =
# #     document.getElementById("username").value;

# #     const password =
# #     document.getElementById("password").value;

# #     if(username === "advait"
# #     && password === "12345"){

# #         document.getElementById("loginBox")
# #         .style.display = "none";

# #         document.getElementById("game")
# #         .style.display = "block";

# #     }else{

# #         document.getElementById("message")
# #         .innerHTML =
# #         "Invalid Username or Password";
# #     }
# # }

# # /* Tic Tac Toe */

# # let currentPlayer = "X";

# # let board = ["","","","","","","","",""];

# # let gameOver = false;

# # const winPatterns = [

# #     [0,1,2],
# #     [3,4,5],
# #     [6,7,8],

# #     [0,3,6],
# #     [1,4,7],
# #     [2,5,8],

# #     [0,4,8],
# #     [2,4,6]
# # ];

# # /* Play */

# # function play(cell,index){

# #     if(board[index] !== "" || gameOver){
# #         return;
# #     }

# #     board[index] = currentPlayer;

# #     cell.innerHTML = currentPlayer;

# #     checkWinner();

# #     currentPlayer =
# #     currentPlayer === "X" ? "O" : "X";

# #     if(!gameOver){

# #         document.getElementById("status")
# #         .innerHTML =
# #         "Player " + currentPlayer + " Turn";
# #     }
# # }

# # /* Winner */

# # function checkWinner(){

# #     for(let pattern of winPatterns){

# #         let a = pattern[0];
# #         let b = pattern[1];
# #         let c = pattern[2];

# #         if(board[a] &&
# #            board[a] === board[b] &&
# #            board[a] === board[c]){

# #             document.getElementById("status")
# #             .innerHTML =
# #             "Player " + board[a] + " Wins!";

# #             gameOver = true;

# #             return;
# #         }
# #     }

# #     if(!board.includes("")){

# #         document.getElementById("status")
# #         .innerHTML = "Draw Game";

# #         gameOver = true;
# #     }
# # }

# # /* Restart */

# # function restartGame(){

# #     board =
# #     ["","","","","","","","",""];

# #     gameOver = false;

# #     currentPlayer = "X";

# #     document.getElementById("status")
# #     .innerHTML =
# #     "Player X Turn";

# #     const cells =
# #     document.querySelectorAll(".cell");

# #     cells.forEach(cell => {
# #         cell.innerHTML = "";
# #     });
# # }

# # </script>

# # </body>
# # </html>
# # """

# # components.html(html_code, height=1300)



# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(
#     page_title="Lamp Tic Tac Toe",
#     layout="centered"
# )

# html_code = """

# <!DOCTYPE html>
# <html>
# <head>

# <style>

# body{
#     margin:0;
#     padding:0;
#     background:#0a0a0a;
#     font-family:Arial;
#     overflow:hidden;
#     color:white;
# }

# /* Main */

# .container{
#     display:flex;
#     flex-direction:column;
#     align-items:center;
#     min-height:100vh;
#     padding-top:20px;
# }

# /* Ceiling */

# .ceiling{
#     width:100%;
#     height:18px;
#     background:#161616;
#     position:absolute;
#     top:0;
# }

# /* Wire */

# .wire{
#     width:4px;
#     height:220px;
#     background:white;
#     position:relative;
#     cursor:pointer;
# }

# /* Pull Ball */

# .knob{
#     width:22px;
#     height:22px;
#     border-radius:50%;
#     background:white;
#     position:absolute;
#     bottom:-10px;
#     left:50%;
#     transform:translateX(-50%);
# }

# /* Lamp */

# .lamp{
#     width:170px;
#     height:85px;
#     background:linear-gradient(to bottom,#555,#111);
#     border-radius:0 0 90px 90px;
#     margin-top:-2px;
#     position:relative;
#     transition:0.5s;
# }

# /* Lamp ON */

# .lamp.on{
#     background:linear-gradient(to bottom,#ffe680,#d4a600);
#     box-shadow:0 0 45px rgba(255,255,180,0.9);
# }

# /* Glow */

# .glow{
#     width:340px;
#     height:340px;
#     background:radial-gradient(circle,
#     rgba(255,240,180,0.55) 0%,
#     rgba(255,240,180,0.18) 35%,
#     transparent 70%);
#     position:absolute;
#     top:70px;
#     left:50%;
#     transform:translateX(-50%);
#     opacity:0;
#     transition:0.7s;
# }

# .glow.show{
#     opacity:1;
# }

# /* Login Box */

# .login-box{
#     width:340px;
#     background:#151515;
#     padding:30px;
#     border-radius:25px;
#     margin-top:60px;
#     opacity:0;
#     transform:translateY(80px);
#     transition:0.8s;
#     box-shadow:0 0 25px rgba(255,255,255,0.08);
# }

# .login-box.show{
#     opacity:1;
#     transform:translateY(0);
# }

# /* Title */

# .title{
#     text-align:center;
#     font-size:32px;
#     margin-bottom:20px;
# }

# /* Inputs */

# input{
#     width:100%;
#     padding:14px;
#     margin-top:15px;
#     border:none;
#     border-radius:12px;
#     background:#242424;
#     color:white;
#     font-size:16px;
# }

# /* Button */

# button{
#     width:100%;
#     padding:14px;
#     margin-top:20px;
#     border:none;
#     border-radius:12px;
#     background:#f7c948;
#     color:black;
#     font-size:18px;
#     font-weight:bold;
#     cursor:pointer;
# }

# /* Message */

# .message{
#     text-align:center;
#     margin-top:15px;
#     color:#ff4d4d;
# }

# /* Game */

# .game{
#     display:none;
#     margin-top:40px;
#     text-align:center;
# }

# /* Board */

# .board{
#     display:grid;
#     grid-template-columns:repeat(3,100px);
#     gap:10px;
#     margin-top:25px;
# }

# /* Cell */

# .cell{
#     width:100px;
#     height:100px;
#     background:#1a1a1a;
#     border-radius:15px;
#     display:flex;
#     align-items:center;
#     justify-content:center;
#     font-size:45px;
#     cursor:pointer;
#     transition:0.2s;
# }

# .cell:hover{
#     background:#262626;
#     transform:scale(1.05);
# }

# /* Status */

# .status{
#     margin-top:25px;
#     font-size:28px;
#     color:#ffe680;
# }

# /* Restart */

# .restart{
#     width:220px;
#     margin-top:25px;
# }

# </style>

# </head>

# <body>

# <div class="ceiling"></div>

# <div class="container">

#     <!-- Wire -->

#     <div class="wire" id="wire">
#         <div class="knob"></div>
#     </div>

#     <!-- Lamp -->

#     <div class="lamp" id="lamp">
#         <div class="glow" id="glow"></div>
#     </div>

#     <!-- Login -->

#     <div class="login-box" id="loginBox">

#         <div class="title">Login</div>

#         <input type="text"
#         id="username"
#         placeholder="Username">

#         <input type="password"
#         id="password"
#         placeholder="Password">

#         <button onclick="login()">
#             Login
#         </button>

#         <div class="message"
#         id="message"></div>

#     </div>

#     <!-- Game -->

#     <div class="game" id="game">

#         <h1>Tic Tac Toe</h1>

#         <div class="board">

#             <div class="cell" data-index="0"></div>
#             <div class="cell" data-index="1"></div>
#             <div class="cell" data-index="2"></div>

#             <div class="cell" data-index="3"></div>
#             <div class="cell" data-index="4"></div>
#             <div class="cell" data-index="5"></div>

#             <div class="cell" data-index="6"></div>
#             <div class="cell" data-index="7"></div>
#             <div class="cell" data-index="8"></div>

#         </div>

#         <div class="status" id="status">
#             Player X Turn
#         </div>

#         <button class="restart"
#         onclick="restartGame()">
#             Restart Game
#         </button>

#     </div>

# </div>

# <script>

# /* Lamp */

# let active = false;

# document.getElementById("wire")
# .addEventListener("click", function(){

#     active = !active;

#     const lamp =
#     document.getElementById("lamp");

#     const glow =
#     document.getElementById("glow");

#     const loginBox =
#     document.getElementById("loginBox");

#     if(active){

#         lamp.classList.add("on");
#         glow.classList.add("show");
#         loginBox.classList.add("show");

#     }else{

#         lamp.classList.remove("on");
#         glow.classList.remove("show");
#         loginBox.classList.remove("show");
#     }
# });

# /* Login */

# function login(){

#     const username =
#     document.getElementById("username").value;

#     const password =
#     document.getElementById("password").value;

#     if(username === "advait"
#     && password === "12345"){

#         document.getElementById("loginBox")
#         .style.display = "none";

#         document.getElementById("game")
#         .style.display = "block";

#     }else{

#         document.getElementById("message")
#         .innerHTML =
#         "Invalid Username or Password";
#     }
# }

# /* Game Logic */

# let currentPlayer = "X";

# let gameActive = true;

# let board = ["","","","","","","","",""];

# const status =
# document.getElementById("status");

# const cells =
# document.querySelectorAll(".cell");

# const winPatterns = [

#     [0,1,2],
#     [3,4,5],
#     [6,7,8],

#     [0,3,6],
#     [1,4,7],
#     [2,5,8],

#     [0,4,8],
#     [2,4,6]
# ];

# /* Cell Click */

# cells.forEach(cell => {

#     cell.addEventListener("click", () => {

#         const index =
#         cell.getAttribute("data-index");

#         if(board[index] !== ""
#         || !gameActive){
#             return;
#         }

#         board[index] = currentPlayer;

#         cell.innerHTML = currentPlayer;

#         checkWinner();

#         if(gameActive){

#             currentPlayer =
#             currentPlayer === "X"
#             ? "O"
#             : "X";

#             status.innerHTML =
#             "Player " +
#             currentPlayer +
#             " Turn";
#         }

#     });

# });

# /* Check Winner */

# function checkWinner(){

#     for(let pattern of winPatterns){

#         let a = pattern[0];
#         let b = pattern[1];
#         let c = pattern[2];

#         if(board[a] &&
#            board[a] === board[b] &&
#            board[a] === board[c]){

#             status.innerHTML =
#             "Player " +
#             board[a] +
#             " Wins!";

#             gameActive = false;

#             return;
#         }
#     }

#     if(!board.includes("")){

#         status.innerHTML =
#         "Draw Game";

#         gameActive = false;
#     }
# }

# /* Restart */

# function restartGame(){

#     board =
#     ["","","","","","","","",""];

#     gameActive = true;

#     currentPlayer = "X";

#     status.innerHTML =
#     "Player X Turn";

#     cells.forEach(cell => {

#         cell.innerHTML = "";

#     });
# }

# </script>

# </body>
# </html>

# """

# components.html(html_code, height=1200)






import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Advait Company",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    padding:0;
    background:#050505;
    overflow:hidden;
    font-family:Arial, sans-serif;
    color:white;
}

/* Intro Screen */

.intro{
    position:fixed;
    width:100%;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    background:#050505;
    z-index:10;
    animation:hideIntro 5s forwards;
    animation-delay:5s;
}

/* Searching Circle */

.circle{
    width:220px;
    height:220px;
    border-radius:50%;
    border:5px solid rgba(255,255,255,0.1);
    border-top:5px solid #ffe680;
    animation:spin 2s linear infinite;
    position:absolute;
}

/* Company Name */

.company{
    font-size:48px;
    font-weight:bold;
    color:#ffe680;
    letter-spacing:4px;
    z-index:2;
    text-shadow:0 0 20px rgba(255,230,120,0.8);
}

/* Hide Intro */

@keyframes hideIntro{

    to{
        opacity:0;
        visibility:hidden;
    }
}

/* Rotate */

@keyframes spin{

    from{
        transform:rotate(0deg);
    }

    to{
        transform:rotate(360deg);
    }
}

/* Main */

.main{
    display:flex;
    flex-direction:column;
    align-items:center;
    min-height:100vh;
    padding-top:20px;
}

/* Ceiling */

.ceiling{
    width:100%;
    height:20px;
    background:#111;
    position:absolute;
    top:0;
}

/* Wire */

.wire{
    width:4px;
    height:230px;
    background:white;
    position:relative;
    cursor:pointer;
    margin-top:40px;
}

/* Pull Ball */

.knob{
    width:24px;
    height:24px;
    border-radius:50%;
    background:white;
    position:absolute;
    bottom:-10px;
    left:50%;
    transform:translateX(-50%);
}

/* Lamp */

.lamp{
    width:180px;
    height:90px;
    background:linear-gradient(to bottom,#555,#111);
    border-radius:0 0 90px 90px;
    margin-top:-2px;
    position:relative;
    transition:0.5s;
}

/* Lamp ON */

.lamp.on{
    background:linear-gradient(to bottom,#ffe680,#d6a700);
    box-shadow:0 0 50px rgba(255,255,180,0.9);
}

/* Glow */

.glow{
    width:350px;
    height:350px;
    background:radial-gradient(circle,
    rgba(255,240,180,0.6) 0%,
    rgba(255,240,180,0.2) 35%,
    transparent 70%);
    position:absolute;
    top:70px;
    left:50%;
    transform:translateX(-50%);
    opacity:0;
    transition:0.8s;
}

.glow.show{
    opacity:1;
}

/* Login Box */

.login-box{
    width:360px;
    background:#141414;
    padding:30px;
    border-radius:25px;
    margin-top:60px;
    opacity:0;
    transform:translateY(80px);
    transition:0.8s;
    box-shadow:0 0 30px rgba(255,255,255,0.08);
}

/* Show Login */

.login-box.show{
    opacity:1;
    transform:translateY(0);
}

/* Title */

.title{
    text-align:center;
    font-size:34px;
    margin-bottom:20px;
    color:#ffe680;
}

/* Inputs */

input{
    width:100%;
    padding:15px;
    margin-top:15px;
    border:none;
    border-radius:12px;
    background:#222;
    color:white;
    font-size:16px;
}

/* Button */

button{
    width:100%;
    padding:15px;
    margin-top:22px;
    border:none;
    border-radius:12px;
    background:#ffe680;
    color:black;
    font-size:18px;
    font-weight:bold;
    cursor:pointer;
}

/* Message */

.message{
    text-align:center;
    margin-top:15px;
    color:#ff4d4d;
}

/* Profile */

.profile{
    display:none;
    margin-top:40px;
    width:420px;
    background:#121212;
    padding:30px;
    border-radius:25px;
    box-shadow:0 0 35px rgba(255,255,255,0.08);
    text-align:center;
}

/* Kid Avatar */

.avatar{
    width:120px;
    height:120px;
    border-radius:50%;
    background:#ffe680;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:60px;
    margin:auto;
    margin-bottom:20px;
}

/* Text */

.profile h1{
    color:#ffe680;
    margin-bottom:10px;
}

.info{
    font-size:20px;
    margin-top:10px;
    opacity:0.9;
}

/* Hobby Box */

.hobby{
    margin-top:25px;
    background:#1f1f1f;
    padding:20px;
    border-radius:15px;
    font-size:20px;
}

/* Toys */

.toys{
    margin-top:20px;
    font-size:40px;
}

</style>

</head>

<body>

<!-- Intro -->

<div class="intro">

    <div class="circle"></div>

    <div class="company">
        ADVAIT AGRO FARMS
    </div>

</div>

<!-- Main -->

<div class="main">

    <div class="ceiling"></div>

    <!-- Wire -->

    <div class="wire" id="wire">
        <div class="knob"></div>
    </div>

    <!-- Lamp -->

    <div class="lamp" id="lamp">
        <div class="glow" id="glow"></div>
    </div>

    <!-- Login -->

    <div class="login-box" id="loginBox">

        <div class="title">
            Secret Login
        </div>

        <input type="text"
        id="username"
        placeholder="Username">

        <input type="password"
        id="password"
        placeholder="Password">

        <button onclick="login()">
            Login
        </button>

        <div class="message"
        id="message"></div>

    </div>

    <!-- Profile -->

    <div class="profile" id="profile">

        <div class="avatar">
            👦
        </div>

        <h1>Advait</h1>

        <div class="info">
            📍 Mumbai
        </div>

        <div class="info">
            🎂 Age : 5
        </div>

        <div class="info">
            🚜 Loves Playing JCB
        </div>

        <div class="info">
            🎮 dont waste time on watching Cartoon and playing mobile Games
        </div>

        <div class="info">
            🍫 dont like to eat Chocolates & junk food
        </div>

        <div class="hobby">
            ⭐ Favorite Hobby:
            Playing with toy trucks,
            JCB machines and racing cars.
        </div>

        <div class="toys">
            🚜 🚗 🧸 🎮 ⚽
        </div>

    </div>

</div>

<script>

/* Lamp */

let active = false;

document.getElementById("wire")
.addEventListener("click", function(){

    active = !active;

    const lamp =
    document.getElementById("lamp");

    const glow =
    document.getElementById("glow");

    const loginBox =
    document.getElementById("loginBox");

    if(active){

        lamp.classList.add("on");
        glow.classList.add("show");
        loginBox.classList.add("show");

    }else{

        lamp.classList.remove("on");
        glow.classList.remove("show");
        loginBox.classList.remove("show");
    }
});

/* Login */

function login(){

    const username =
    document.getElementById("username").value;

    const password =
    document.getElementById("password").value;

    if(username === "advait"
    && password === "12345"){

        document.getElementById("loginBox")
        .style.display = "none";

        document.getElementById("profile")
        .style.display = "block";

    }else{

        document.getElementById("message")
        .innerHTML =
        "Invalid Username or Password";
    }
}

</script>

</body>
</html>

"""

components.html(html_code, height=1300)


