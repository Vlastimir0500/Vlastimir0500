<svg xmlns="http://www.w3.org/2000/svg"
width="1200"
height="350"
viewBox="0 0 1200 350">

<defs>

<linearGradient id="bg"
x1="0%"
y1="0%"
x2="100%"
y2="100%">

<stop offset="0%" stop-color="#090d13"/>
<stop offset="100%" stop-color="#121821"/>

</linearGradient>

<radialGradient id="titleGlow"
cx="25%"
cy="35%"
r="65%">

<stop offset="0%" stop-color="#58a6ff" stop-opacity=".22"/>
<stop offset="100%" stop-color="#58a6ff" stop-opacity="0"/>

</radialGradient>

<filter id="glow">

<feGaussianBlur
stdDeviation="4"
result="blur"/>

<feMerge>

<feMergeNode in="blur"/>
<feMergeNode in="SourceGraphic"/>

</feMerge>

</filter>

<pattern
id="grid"
width="40"
height="40"
patternUnits="userSpaceOnUse">

<path
d="M40 0H0V40"
fill="none"
stroke="#1d2634"
stroke-width="1"/>

</pattern>

<style>

text{
font-family:
"JetBrains Mono",
"Fira Code",
Consolas,
monospace;
}

.title{
fill:#ffffff;
font-size:42px;
}

.name{
fill:#58a6ff;
font-size:62px;
font-weight:bold;
}

.sub{
fill:#8b949e;
font-size:20px;
}

.prompt{
fill:#3fb950;
font-size:18px;
}

.cursor{
fill:#58a6ff;
animation:blink 1s steps(1) infinite;
}

@keyframes blink{

50%{
opacity:0;
}

}

</style>

</defs>

<!-- Background -->

<rect
width="1200"
height="350"
fill="url(#bg)"/>

<rect
width="1200"
height="350"
fill="url(#grid)"
opacity=".10"/>

<rect
width="1200"
height="350"
fill="url(#titleGlow)"/>

<!-- Stars -->

<g
fill="#58a6ff"
opacity=".35">

<circle cx="95" cy="40" r="1"/>
<circle cx="240" cy="70" r="1.3"/>
<circle cx="410" cy="30" r="1"/>
<circle cx="590" cy="95" r="1.4"/>
<circle cx="770" cy="45" r="1"/>
<circle cx="960" cy="65" r="1.2"/>
<circle cx="1120" cy="40" r="1"/>

<circle cx="1020" cy="300" r="1"/>
<circle cx="870" cy="250" r="1.3"/>
<circle cx="680" cy="285" r="1"/>

</g>

<!-- Title -->

<text
x="60"
y="78"
class="title">

&gt; whoami

</text>

<text
x="60"
y="136"
class="name"
filter="url(#glow)">

VLASTIMIR

</text>

<text
x="60"
y="172"
class="sub">

AI • Cybersecurity • Python • Open Source

</text>

<rect
x="520"
y="92"
width="12"
height="44"
class="cursor"/>

<!-- Scan Line -->

<line
x1="0"
y1="190"
x2="1200"
y2="190"
stroke="#58a6ff"
stroke-opacity=".15">

<animate
attributeName="y1"
values="0;350;0"
dur="8s"
repeatCount="indefinite"/>

<animate
attributeName="y2"
values="0;350;0"
dur="8s"
repeatCount="indefinite"/>

</line>
<!-- ================= TERMINAL ================= -->

<rect
x="60"
y="210"
width="470"
height="105"
rx="12"
fill="#070b12"
stroke="#2b3547"/>

<!-- Terminal Bar -->

<rect
x="60"
y="210"
width="470"
height="26"
rx="12"
fill="#0f1522"/>

<circle cx="82" cy="223" r="4" fill="#ff5f56"/>
<circle cx="98" cy="223" r="4" fill="#ffbd2e"/>
<circle cx="114" cy="223" r="4" fill="#27c93f"/>

<text
x="290"
y="227"
text-anchor="middle"
fill="#6b778f"
font-size="12">

terminal

</text>

<!-- Terminal Text -->

<text
x="82"
y="258"
class="prompt">

$ python profile.py

</text>

<text
x="82"
y="283"
fill="#dce7ff"
font-size="17">

Building GitHub profile...

</text>

<text
x="82"
y="308"
class="prompt">

$ █

</text>

<!-- ================= RIGHT PANEL ================= -->

<text
x="660"
y="70"
fill="#58a6ff"
font-size="22"
font-weight="700"
filter="url(#glow)">

RESEARCH

</text>

<line
x1="660"
y1="82"
x2="1110"
y2="82"
stroke="#2d384d"/>

<text
x="660"
y="120"
fill="#ffffff"
font-size="18">

Neural Networks

</text>

<text
x="660"
y="152"
fill="#ffffff"
font-size="18">

Artificial Intelligence

</text>

<text
x="660"
y="184"
fill="#ffffff"
font-size="18">

Cybersecurity

</text>

<text
x="660"
y="216"
fill="#ffffff"
font-size="18">

Python Automation

</text>

<text
x="660"
y="248"
fill="#ffffff"
font-size="18">

Open Source

</text>

<!-- Divider -->

<line
x1="620"
y1="45"
x2="620"
y2="305"
stroke="#273244"/>
<!-- ================= NEURAL NETWORK ================= -->

<g stroke="#58a6ff"
stroke-width="1.5"
opacity=".45">

<line x1="760" y1="95" x2="860" y2="140"/>
<line x1="760" y1="185" x2="860" y2="140"/>
<line x1="860" y1="140" x2="970" y2="100"/>
<line x1="860" y1="140" x2="970" y2="185"/>
<line x1="970" y1="100" x2="1085" y2="145"/>
<line x1="970" y1="185" x2="1085" y2="145"/>

</g>

<g fill="#58a6ff" filter="url(#glow)">

<circle cx="760" cy="95" r="5">
<animate attributeName="r"
values="5;7;5"
dur="2.3s"
repeatCount="indefinite"/>
</circle>

<circle cx="760" cy="185" r="5">
<animate attributeName="r"
values="5;7;5"
dur="2.9s"
repeatCount="indefinite"/>
</circle>

<circle cx="860" cy="140" r="6">
<animate attributeName="r"
values="6;8;6"
dur="2.1s"
repeatCount="indefinite"/>
</circle>

<circle cx="970" cy="100" r="5">
<animate attributeName="r"
values="5;7;5"
dur="2.7s"
repeatCount="indefinite"/>
</circle>

<circle cx="970" cy="185" r="5">
<animate attributeName="r"
values="5;7;5"
dur="3.1s"
repeatCount="indefinite"/>
</circle>

<circle cx="1085" cy="145" r="7">
<animate attributeName="r"
values="7;10;7"
dur="2.5s"
repeatCount="indefinite"/>
</circle>

</g>

<!-- Floating particles -->

<g fill="#58a6ff" opacity=".45">

<circle cx="1115" cy="250" r="2">
<animate attributeName="cy"
values="250;220;250"
dur="5s"
repeatCount="indefinite"/>
</circle>

<circle cx="1035" cy="310" r="2">
<animate attributeName="cy"
values="310;270;310"
dur="4s"
repeatCount="indefinite"/>
</circle>

<circle cx="930" cy="280" r="1.5">
<animate attributeName="cy"
values="280;245;280"
dur="6s"
repeatCount="indefinite"/>
</circle>

</g>

<!-- Footer -->

<line
x1="40"
y1="332"
x2="1160"
y2="332"
stroke="#283245"
opacity=".6"/>

<text
x="600"
y="345"
text-anchor="middle"
fill="#6f7f9d"
font-size="14"
letter-spacing="2">

COMPUTE • BUILD • RESEARCH • LEARN

</text>

</svg>
