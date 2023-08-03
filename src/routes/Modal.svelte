<script>
	export let showModal; // boolean

	let dialog; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();

    import Button, { Label } from '@smui/button';

    //to_top.scrollIntoView()
    import { Svrollbar } from 'svrollbar'

    export let viewport
    export let contents

</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
    class="glossary-modal"
    
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div on:click|stopPropagation class="glossary-modal">
		<!-- <slot name="header"/> -->

        <div bind:this={viewport} class="viewport">
        <div bind:this={contents} class="contents">
        <div class="glossary-modal">


            <h3>
                Glossary
            </h3>
            <p>
                The glossary briefly reviews the available sql dialects.
            </p>
        
                <p class="code">
                    <b>tsql</b>: Microsoft Sql Server dialect. All applications that communicate with an instance of SQL Server do so by sending Transact-SQL statements to the server, regardless of the user interface of the application.
                </p>
        
                <p>
                    Example:
                </p>
        
                
<pre class="code">    INSERT dbo.Products (ProductName, ProductID, Price, ProductDescription) 
        VALUES ('Screwdriver', 50, 3.17, 'Flat head') </pre>
        
                <br/>
        
                <p>
                    <b> teradata: </b> Terradata flavor of SQL. 
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO database_name.tbl_2 (column_1,column_2,..,column_n)
        SELECT (column_1,column_2,..,column_n) from database_name.tbl_2;
                </pre>
        
                <br/>
        
                <p>
                    <b> oracle: </b> For interacting with Oracle databases
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO AIRPORTS (AIRPORT, CITY, COUNTRY)
        SELECT AIRPORT, CITY_NAME, COUNTRY FROM CITIES;
                </pre>
        
                <br/>
        
                <p>
                    <b> snowflake: </b> Why aren't you using Snowflake yet?
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO employees(first_name, last_name, workphone, city,postal_code)
    SELECT
        contractor_first,contractor_last,worknum,NULL,zip_code
    FROM contractors
                </pre>
        
                <br/>
        
                <p>
                    <b> biquery: </b> BigQuery is Google's fully managed, serverless data warehouse 
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT dataset.DetailedInventory (product, quantity, supply_constrained)
    SELECT product, quantity, false
    FROM dataset.Inventory    
                </pre>
        
                <br/>
        
                <p>
                    <b> databricks: </b>  serverless data warehouse on the Databricks Lakehouse Platform
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO students PARTITION (student_id = 444444)
    SELECT name, address FROM person;
                </pre>
        
                <br/>
                
                <p class="code">
                    <b> redshift: </b> Amazon Redshift is built around industry-standard SQL, with added functionality to manage very large datasets
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    insert into category_stage
    (select * from category);
                </pre>
        
                <br/>
        
                <p class="code">
                    <b> sqllite: </b> SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO prod_backup SELECT * FROM prod_mast;
                </pre>
        
                <br/>
        
                <p>
                    <b> mysql: </b> MySQL is an open-source relational database management system
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO table2
    SELECT * FROM table1
                </pre>
        
                <br/>
        
                <p class="code">
                    <b> postgres: </b>  free and open-source relational database management system emphasizing extensibility and SQL compliance
                </p>
        
                <p>
                    Example:
                </p>
        
                <pre class="code">
    INSERT INTO films SELECT * FROM tmp_films
                </pre>
        
            </div>

		<!-- svelte-ignore a11y-autofocus -->
		<Button autofocus on:click={() => dialog.close()}>Close</Button>
	</div>
    </div>
    
    </div>
    <slot />
    <Svrollbar {viewport} {contents} />
</dialog>

<style>
	dialog {
		max-width: 1000px;
        width: 1000px;
		border: none;
		padding: 0;
        border-radius: 20px;
        background: linear-gradient(138deg, rgba(255, 215, 99, 0.50) 0%, rgba(255, 220, 121, 0.10) 100%);
        box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        color:white;


	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}



    .wrapper {
    position: relative;
    width: 10rem;
  }

  .viewport {
    position: relative;
    width: 100rem;
    height: 100rem;
    overflow: scroll;
    box-sizing: border-box;

    /* hide scrollbar */
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .viewport::-webkit-scrollbar {
    /* hide scrollbar */
    display: none;
  }


  .glossary-modal {
    /* hide scrollbar */
    -ms-overflow-style: none;
    scrollbar-width: none;
    overflow: scroll;
    width: 800px;

  }

  .glossary-modal::-webkit-scrollbar {
    /* hide scrollbar */
    display: none;
  }

  .code {
    width: 700px;
  }

</style>