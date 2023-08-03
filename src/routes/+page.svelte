
<script>
    //placeholder
    import CodeInput from './code_input.svelte';
    import CodeUpload from './code_upload.svelte';

</script>

<svelte:head>
	<title>SQL Convert</title>
	<meta name="description" content="Sql convert page" />
</svelte:head>

<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; padding-top:100px">
	<img src="convert_images/full_logo.svg" style="width:500px"/>

	<p>
		<b>Secure. Open Source. Always Free. </b>
	</p>
	<p>
		Enter your SQL text and select the SQL Dialects or bulk upload files 
	</p>

</div>


<section>
	<div style="display:flex; flex-direction:row;">
		<div style="display:flex; flex-grow:2; flex-direction:column; width:50%; padding: 20px;">
			<CodeInput />
		</div>
		
		<div style="display:flex; flex-grow:2; flex-direction:column; width:50%; padding: 20px;">
			<CodeUpload />
		</div>
	</div>
    
</section>



<style>
	h1 {
		color: white;
	}
	p {
		color: white;
	}

</style>
