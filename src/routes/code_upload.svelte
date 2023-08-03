<script lang = ts  src="https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js">



    import Card, {
        Content,
        PrimaryAction,
        Media,
        MediaContent,
    } from '@smui/card';

    //styling
    import Button, { Label } from '@smui/button';
    import Select, { Option } from '@smui/select';
    import CircularProgress from '@smui/circular-progress';

    import { pyodide_status, pyodide_load }  from './stores.js';
    import { get } from 'svelte/store';



    let files;
    let fileinput;

    $: if (files) {
        console.log(files)

        for (const file of files) {
            console.log(`${file.name}: ${file.size} bytes`)
        }
    }


    let supported_dialects = ['tsql', 'snowflake', 'oracle'];
    let input_dialect = 'tsql';
    let target_dialect = 'snowflake';


    let pyodide;
    let pyodide_loaded = false;

    let returned_files = [];
    let show_card = false;
    let display_loading = false;





    async function handle_files() {
        display_loading = true;

        //let sql_namespace = {sql_files: files[0]};
        let sql_file_namespace = [];

        for (const file of files) {
            let file_name = file.name
            let file_text = await file.text()
            sql_file_namespace.push({file_name: file_name, 
                file_contents: file_text,
                input_dialect: input_dialect,
                target_dialect: target_dialect})
        }

        console.log("namespace var: ", sql_file_namespace)

        //console.log(files[0])

        pyodide_loaded = get(pyodide_status);
        if (!pyodide_loaded) {
            pyodide = await loadPyodide();
            pyodide_status.set(true);
            console.log("loaded pyodide");
            pyodide_load.set(pyodide);
        } 

        pyodide = get(pyodide_load)

        //pyodide.FS.writeFile("sql_example.txt", files[0])
        console.log("namespace for pyodide: ", sql_file_namespace)
        await pyodide.registerJsModule("sql_file_namespace", sql_file_namespace);

        await pyodide.loadPackage('micropip')


        const py_sql_convert_path = await fetch("sql_convert_files.py")
        const py_script_text = await py_sql_convert_path.text()

        // console.log(script_text)

        await pyodide.runPythonAsync(py_script_text)

        // console.log("converted objects:  ", converted_query.toJs())

        for (let x of converted_query.toJs().entries()) {
            //console.log(x[1])
            console.log(x[1].get("file_name"))
            console.log(x[1].get("converted_sql"))

            generate_links(x[1].get("file_name"), x[1].get("converted_sql"))

        }

        display_loading = false;
        
    }

    function generate_links(file_name, converted_sql) {

        let temp_file = new File([converted_sql], file_name, {type: 'application/text'});
        let file_url = URL.createObjectURL(temp_file);

        returned_files.push({name: file_name.split(".txt")[0] + `_converted.txt`,
                             url: file_url
                            })

        new_files = returned_files

        console.log(new_files)

        show_card = true
    }




    $: new_files = returned_files;
    $: show_card = show_card;
    $: display_loading = display_loading;

    // may need to:
    // 1. read files to text - js
    // 2. pass text to python - both
    // 3. convert and return text - both
    // 4. convert text back to files - js
    // (ideally would handle as much as possible in python)

</script>


<div > 
    <h3 style="padding-top:5px;"> 
        Upload Files 
    </h3>

    <Card padded style="display:flex; justify-content:center; align-items:center;padding-top:90px;padding-bottom:90px;">

            <!-- <img class = "upload" src="https://static.thenounproject.com/png/625182-200.png" alt="" on:click={()=>{files.click();}} />
            <div on:click={()=>{files.click();}}>Choose SQL Files</div> -->

            <label for="sql_upload" >
                <img class="upload-effect" src="convert_images/sql_upload_img.png"/>
            </label>

            <input accept=".sql,.txt" bind:files id = "sql_upload" multiple  name = "sql_upload" type="file" style="display:none"/>

            {#if files}
                <h2>
                    selected files:
                </h2>
            {#each Array.from(files) as file}
                <p>{file.name} ({file.size} bytes)</p>
            {/each}
            {/if}

    </Card>
</div>

<div style="padding: 20px">
    <Select bind:value = {input_dialect} label = "Select Input Dialect">
        {#each supported_dialects as dialect}
        <Option value = {dialect}> {dialect} </Option>
        {/each}
    </Select>    
    
    <Select bind:value = {target_dialect} label = "Select Target Dialect">
        {#each supported_dialects as dialect}
        <Option value = {dialect}> {dialect} </Option>
        {/each}
    </Select>  

    <Button on:click={ handle_files } variant="raised">
        <Label> Convert </Label>
    </Button>

</div>

{#if display_loading}
<div style="display:flex; flex-grow:1; flex-direction:column; width:90%; padding: 20px;">

    <CircularProgress style="height: 32px; width: 32px;" indeterminate />
    <p>
        *first run takes longer, subsequent runs go faster
    </p>
</div>
{/if}


<div>
    {#if show_card}
    <Card padded style="display:flex; direction:column; justify-content:right; align-items:center;">
        {#each new_files as item }
        <p>
            <a href={item.url} target="_blank" download={item.name}> {item.name}</a>
        </p>
        {/each}
    </Card>
    {/if}

</div>

<style>

.upload-effect {
    width:150px;
    filter: drop-shadow(0px 2px 2px rgba(0, 0, 0, 0.25));
    padding:10px;
    border-radius: 10px;
}

.upload-effect:hover {
    background-color: #48515B;
}

.upload-effect:active {
    padding: 0;
    margin: 0;
    opacity: 1;
    transition: 0s
}

.upload-effect:after {
  content: "";
  background: #90EE90;
  display: block;
  position: absolute;
  padding-top: 100%;
  padding-left: 100%;
  margin-left: -5px!important;
  margin-top: -105%;
  opacity: 0;
  transition: all 0.8s
}

</style>