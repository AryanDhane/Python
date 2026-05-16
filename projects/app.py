# # import streamlit as st
# # import streamlit.components.v1 as components

# # st.set_page_config(
# #     page_title="Hidden Lamp Login",
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
# #     background:#0d0d0d;
# #     overflow:hidden;
# #     font-family:Arial, sans-serif;
# # }

# # /* Main Container */

# # .container{
# #     display:flex;
# #     flex-direction:column;
# #     align-items:center;
# #     justify-content:flex-start;
# #     height:100vh;
# #     padding-top:20px;
# # }

# # /* Ceiling */

# # .ceiling{
# #     width:100%;
# #     height:20px;
# #     background:#1f1f1f;
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
# #     width:22px;
# #     height:22px;
# #     border-radius:50%;
# #     background:#f2f2f2;
# #     position:absolute;
# #     bottom:-10px;
# #     left:50%;
# #     transform:translateX(-50%);
# #     box-shadow:0 0 10px rgba(255,255,255,0.5);
# # }

# # /* Lamp */

# # .lamp{
# #     width:160px;
# #     height:80px;
# #     background:linear-gradient(to bottom,#555,#111);
# #     border-radius:0 0 80px 80px;
# #     margin-top:-2px;
# #     position:relative;
# #     transition:0.5s;
# # }

# # /* Lamp ON */

# # .lamp.on{
# #     background:linear-gradient(to bottom,#ffe680,#d4a900);
# #     box-shadow:0 0 40px rgba(255,255,180,0.9);
# # }

# # /* Light Glow */

# # .glow{
# #     width:320px;
# #     height:320px;
# #     background:radial-gradient(circle,
# #     rgba(255,255,180,0.55) 0%,
# #     rgba(255,255,180,0.2) 35%,
# #     transparent 70%);
# #     position:absolute;
# #     top:70px;
# #     left:50%;
# #     transform:translateX(-50%);
# #     opacity:0;
# #     transition:0.7s;
# # }

# # /* Glow Visible */

# # .glow.show{
# #     opacity:1;
# # }

# # /* Login Box */

# # .login-box{
# #     width:340px;
# #     background:#161616;
# #     padding:30px;
# #     border-radius:20px;
# #     margin-top:60px;
# #     opacity:0;
# #     transform:translateY(80px);
# #     transition:0.8s;
# #     box-shadow:0 0 25px rgba(255,255,255,0.08);
# # }

# # /* Show Login */

# # .login-box.show{
# #     opacity:1;
# #     transform:translateY(0);
# # }

# # /* Title */

# # .title{
# #     text-align:center;
# #     color:white;
# #     font-size:28px;
# #     margin-bottom:20px;
# #     font-weight:bold;
# # }

# # /* Inputs */

# # input{
# #     width:100%;
# #     padding:14px;
# #     margin-top:15px;
# #     border:none;
# #     border-radius:10px;
# #     background:#262626;
# #     color:white;
# #     font-size:16px;
# # }

# # /* Button */

# # button{
# #     width:100%;
# #     padding:14px;
# #     margin-top:20px;
# #     border:none;
# #     border-radius:10px;
# #     background:#f7c948;
# #     color:black;
# #     font-size:18px;
# #     font-weight:bold;
# #     cursor:pointer;
# #     transition:0.3s;
# # }

# # button:hover{
# #     transform:scale(1.03);
# # }

# # /* Message */

# # .message{
# #     margin-top:15px;
# #     text-align:center;
# #     font-size:15px;
# # }

# # /* Responsive */

# # @media(max-width:500px){

# #     .lamp{
# #         width:120px;
# #         height:60px;
# #     }

# #     .wire{
# #         height:200px;
# #     }

# #     .login-box{
# #         width:90%;
# #     }

# #     .glow{
# #         width:240px;
# #         height:240px;
# #     }
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

# #     <!-- Login Box -->
# #     <div class="login-box" id="loginBox">

# #         <div class="title">Login</div>

# #         <input type="text" id="username" placeholder="Username">

# #         <input type="password" id="password" placeholder="Password">

# #         <button onclick="login()">Login</button>

# #         <div class="message" id="message"></div>

# #     </div>

# # </div>

# # <script>

# # let active = false;

# # document.getElementById("wire").addEventListener("click", function(){

# #     const lamp = document.getElementById("lamp");
# #     const glow = document.getElementById("glow");
# #     const loginBox = document.getElementById("loginBox");

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

# # function login(){

# #     const username = document.getElementById("username").value;
# #     const password = document.getElementById("password").value;

# #     const message = document.getElementById("message");

# #     if(username === "admin" && password === "1234"){

# #         message.style.color = "#00ff99";
# #         message.innerHTML = "Login Successful";

# #     }else{

# #         message.style.color = "#ff4d4d";
# #         message.innerHTML = "Invalid Username or Password";
# #     }
# # }

# # </script>

# # </body>
# # </html>
# # """

# # components.html(html_code, height=950)





# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(
#     page_title="Lamp Secret Game",
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
#     background:#0d0d0d;
#     overflow:hidden;
#     font-family:Arial, sans-serif;
# }

# /* Main Container */

# .container{
#     display:flex;
#     flex-direction:column;
#     align-items:center;
#     justify-content:flex-start;
#     height:100vh;
#     padding-top:20px;
# }

# /* Ceiling */

# .ceiling{
#     width:100%;
#     height:20px;
#     background:#1c1c1c;
#     position:absolute;
#     top:0;
# }

# /* Wire */

# .wire{
#     width:4px;
#     height:240px;
#     background:white;
#     position:relative;
#     cursor:pointer;
# }

# /* Pull Ball */

# .knob{
#     width:22px;
#     height:22px;
#     border-radius:50%;
#     background:#f1f1f1;
#     position:absolute;
#     bottom:-10px;
#     left:50%;
#     transform:translateX(-50%);
#     box-shadow:0 0 10px rgba(255,255,255,0.5);
# }

# /* Lamp */

# .lamp{
#     width:170px;
#     height:85px;
#     background:linear-gradient(to bottom,#555,#111);
#     border-radius:0 0 90px 90px;
#     position:relative;
#     margin-top:-2px;
#     transition:0.5s;
# }

# /* Lamp ON */

# .lamp.on{
#     background:linear-gradient(to bottom,#ffe680,#c79a00);
#     box-shadow:0 0 45px rgba(255,255,180,0.9);
# }

# /* Glow */

# .glow{
#     width:340px;
#     height:340px;
#     background:radial-gradient(circle,
#     rgba(255,255,180,0.6) 0%,
#     rgba(255,255,180,0.2) 35%,
#     transparent 70%);
#     position:absolute;
#     top:75px;
#     left:50%;
#     transform:translateX(-50%);
#     opacity:0;
#     transition:0.8s;
# }

# .glow.show{
#     opacity:1;
# }

# /* Login Box */

# .login-box{
#     width:340px;
#     background:#151515;
#     padding:30px;
#     border-radius:20px;
#     margin-top:60px;
#     opacity:0;
#     transform:translateY(80px);
#     transition:0.8s;
#     box-shadow:0 0 25px rgba(255,255,255,0.08);
# }

# /* Show Login */

# .login-box.show{
#     opacity:1;
#     transform:translateY(0);
# }

# /* Title */

# .title{
#     text-align:center;
#     color:white;
#     font-size:30px;
#     margin-bottom:20px;
#     font-weight:bold;
# }

# /* Inputs */

# input{
#     width:100%;
#     padding:14px;
#     margin-top:15px;
#     border:none;
#     border-radius:10px;
#     background:#262626;
#     color:white;
#     font-size:16px;
# }

# /* Button */

# button{
#     width:100%;
#     padding:14px;
#     margin-top:20px;
#     border:none;
#     border-radius:10px;
#     background:#f7c948;
#     color:black;
#     font-size:18px;
#     font-weight:bold;
#     cursor:pointer;
#     transition:0.3s;
# }

# button:hover{
#     transform:scale(1.03);
# }

# /* Message */

# .message{
#     margin-top:15px;
#     text-align:center;
#     font-size:15px;
# }

# /* Game Box */

# .game-box{
#     display:none;
#     margin-top:50px;
#     text-align:center;
#     color:white;
# }

# /* Game Button */

# .game-btn{
#     width:180px;
#     margin-top:25px;
# }

# /* Score */

# .score{
#     margin-top:20px;
#     font-size:26px;
#     color:#ffe680;
# }

# /* Responsive */

# @media(max-width:500px){

#     .lamp{
#         width:120px;
#         height:60px;
#     }

#     .wire{
#         height:200px;
#     }

#     .login-box{
#         width:90%;
#     }

#     .glow{
#         width:240px;
#         height:240px;
#     }
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

#         <input type="text" id="username" placeholder="Username">

#         <input type="password" id="password" placeholder="Password">

#         <button onclick="login()">Login</button>

#         <div class="message" id="message"></div>

#     </div>

#     <!-- Secret Game -->
#     <div class="game-box" id="gameBox">

#         <h1>Secret Click Game</h1>

#         <p>Click the button and increase your score.</p>

#         <button class="game-btn" onclick="increaseScore()">
#             Click Me
#         </button>

#         <div class="score" id="score">
#             Score : 0
#         </div>

#     </div>

# </div>

# <script>

# let active = false;
# let score = 0;

# /* Pull Wire */

# document.getElementById("wire").addEventListener("click", function(){

#     const lamp = document.getElementById("lamp");
#     const glow = document.getElementById("glow");
#     const loginBox = document.getElementById("loginBox");

#     active = !active;

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

#     const username = document.getElementById("username").value;
#     const password = document.getElementById("password").value;

#     const message = document.getElementById("message");

#     if(username === "advait" && password === "12345"){

#         document.getElementById("loginBox").style.display = "none";

#         document.getElementById("gameBox").style.display = "block";

#     }else{

#         message.style.color = "#ff4d4d";
#         message.innerHTML = "Invalid Username or Password";
#     }
# }

# /* Game */

# function increaseScore(){

#     score++;

#     document.getElementById("score").innerHTML =
#         "Score : " + score;
# }

# </script>

# </body>
# </html>
# """

# components.html(html_code, height=1000)







import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lamp TikTok Game",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    padding:0;
    background:#0c0c0c;
    overflow:hidden;
    font-family:Arial, sans-serif;
}

/* Main */

.container{
    display:flex;
    flex-direction:column;
    align-items:center;
    height:100vh;
    padding-top:20px;
}

/* Ceiling */

.ceiling{
    width:100%;
    height:20px;
    background:#1a1a1a;
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
}

/* Knob */

.knob{
    width:22px;
    height:22px;
    border-radius:50%;
    background:white;
    position:absolute;
    bottom:-10px;
    left:50%;
    transform:translateX(-50%);
}

/* Lamp */

.lamp{
    width:170px;
    height:85px;
    background:linear-gradient(to bottom,#555,#111);
    border-radius:0 0 90px 90px;
    margin-top:-2px;
    transition:0.5s;
    position:relative;
}

/* Lamp ON */

.lamp.on{
    background:linear-gradient(to bottom,#ffe680,#c89d00);
    box-shadow:0 0 45px rgba(255,255,180,0.9);
}

/* Glow */

.glow{
    width:340px;
    height:340px;
    background:radial-gradient(circle,
    rgba(255,255,180,0.55) 0%,
    rgba(255,255,180,0.18) 35%,
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

/* Login */

.login-box{
    width:340px;
    background:#161616;
    padding:30px;
    border-radius:20px;
    margin-top:60px;
    opacity:0;
    transform:translateY(80px);
    transition:0.8s;
    box-shadow:0 0 20px rgba(255,255,255,0.08);
}

.login-box.show{
    opacity:1;
    transform:translateY(0);
}

/* Title */

.title{
    color:white;
    text-align:center;
    font-size:30px;
    margin-bottom:20px;
}

/* Inputs */

input{
    width:100%;
    padding:14px;
    margin-top:15px;
    border:none;
    border-radius:10px;
    background:#252525;
    color:white;
    font-size:16px;
}

/* Buttons */

button{
    width:100%;
    padding:14px;
    margin-top:20px;
    border:none;
    border-radius:10px;
    background:#f7c948;
    color:black;
    font-size:18px;
    font-weight:bold;
    cursor:pointer;
}

/* Error */

.message{
    text-align:center;
    margin-top:15px;
    color:#ff4d4d;
}

/* TikTok Game */

.game{
    display:none;
    margin-top:40px;
    text-align:center;
    color:white;
}

/* Game Grid */

.grid{
    display:grid;
    grid-template-columns:repeat(3,100px);
    gap:10px;
    margin-top:20px;
}

/* Box */

.box{
    width:100px;
    height:100px;
    background:#1f1f1f;
    border-radius:15px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:40px;
    cursor:pointer;
    transition:0.2s;
}

.box:hover{
    transform:scale(1.05);
}

/* Score */

.score{
    margin-top:20px;
    font-size:24px;
    color:#ffe680;
}

</style>

</head>

<body>

<div class="ceiling"></div>

<div class="container">

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

        <div class="title">Login</div>

        <input type="text" id="username" placeholder="Username">

        <input type="password" id="password" placeholder="Password">

        <button onclick="login()">Login</button>

        <div class="message" id="message"></div>

    </div>

    <!-- TikTok Game -->
    <div class="game" id="game">

        <h1>Tik Tok Game</h1>

        <p>Catch the TikTok icons before they disappear.</p>

        <div class="grid">

            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>

            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>

            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>
            <div class="box" onclick="catchTikTok(this)"></div>

        </div>

        <div class="score" id="score">
            Score : 0
        </div>

    </div>

</div>

<script>

let active = false;
let score = 0;
let currentBox = null;

/* Pull Wire */

document.getElementById("wire").addEventListener("click", function(){

    const lamp = document.getElementById("lamp");
    const glow = document.getElementById("glow");
    const loginBox = document.getElementById("loginBox");

    active = !active;

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

    if(username === "advait" &&
       password === "12345"){

        document.getElementById("loginBox")
            .style.display = "none";

        document.getElementById("game")
            .style.display = "block";

        startGame();

    }else{

        document.getElementById("message")
            .innerHTML =
            "Invalid Username or Password";
    }
}

/* TikTok Game */

function startGame(){

    const boxes =
        document.querySelectorAll(".box");

    setInterval(() => {

        boxes.forEach(box => {
            box.innerHTML = "";
        });

        let random =
            Math.floor(Math.random() * boxes.length);

        currentBox = boxes[random];

        currentBox.innerHTML = "🎵";

    }, 800);
}

/* Catch */

function catchTikTok(box){

    if(box === currentBox &&
       box.innerHTML === "🎵"){

        score++;

        document.getElementById("score")
            .innerHTML =
            "Score : " + score;

        box.innerHTML = "";
    }
}

</script>

</body>

</html>
"""

components.html(html_code, height=1200)