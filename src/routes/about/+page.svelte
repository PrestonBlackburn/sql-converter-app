<script>
	import svelte from '$lib/images/svelte-logo.svg';
	import wasm from '$lib/images/web_assembly.png';
	import sqlglot from '$lib/images/sqlglot.svg';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>


<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; padding-top:100px">
	<img src="convert_images/full_logo.svg" style="width:500px"/>

	<p>
		<b>Secure. Open Source. Always Free. </b>
	</p>

</div>




<div>
	<br/>
	<br/>

	<h1>About</h1>

	<br/>



	<p>
		<b> Secure</b> - Your inputs/data never leaves your machine. Unlike other converters or Chat GPT, you are always in full control of your sql text. 
		This app leveraes WebAssembly to move all of the compute to your browser and avoid needing a backend. 

	</p>

	<br/>

	<p>
		<b> Open Source</b> - This app is open source for maximum transparency. You can look at the source code on my git repo. 

	</p>

	<br/>

	<p>
		<b> Always Free</b> - Since this app has no backend there are virtually no hosting costs. 

	</p>

	<br/>


	<h3>
		How does it work?
	</h3>

	<p>
		The main components of this app are Svelte for the frontend, Pyodide for python using web assembly, and SQLGlot to handle the SQL transformations. 
	</p>

		<br/>
			<h3>
				<img src={svelte} alt="Svelte" style="width:25px;" />  Svelte 
			</h3> 
		<ul>
			<li>
				Svelte is a new way to build web applications. It's a compiler that takes your declarative components and converts them into efficient JavaScript that surgically updates the DOM.
			</li>
			<li>
				<p>Github: <a href="https://github.com/sveltejs/svelte" target="_blank">https://github.com/sveltejs/svelte</a></p>
			</li>
		</ul>

		<br/>
		<h3>
			<img src={wasm} alt="Wasm" style="width:25px;" />  Pyodide 
		</h3> 
		<ul>
			<li>
				Pyodide is a Python distribution for the browser and Node.js based on WebAssembly. Pyodide makes it possible to install and run Python packages in the browser with micropip
			</li>
			<li>
				<p>Github: <a href="https://github.com/pyodide/pyodide" target="_blank">https://github.com/pyodide/pyodide</a></p>
			</li>
		</ul>

		<br/>
		<h3>
			<img src={sqlglot} alt="Wasm" style="width:25px;" />  SqlGlot 
		</h3> 
		<ul>
			<li>
				SQLGlot is a no-dependency SQL parser, transpiler, optimizer, and engine. It can be used to format SQL or translate between 19 different dialects. This runs in the browser by using WebAssembly with pydodide. 
			</li>
			<li>
				<p>Github: <a href="https://github.com/tobymao/sqlglot" target="_blank">https://github.com/tobymao/sqlglot</a></p>
			</li>
		</ul>
	
	
	<br/>
	<br/>
	
	<h3>
		Web Assembly
	</h3>

	<p>
		WebAssembly (Wasm) is designed as a portable compilation target for programming languages, enabling deployment on the web for client and server applications. In this case it enables us to run python in the browser.
	</p>




</div>
