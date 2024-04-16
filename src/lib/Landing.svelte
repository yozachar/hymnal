<script lang="ts">
  // local
  import SearchBox from "./SearchBox.svelte";

  let searchTerm = "";

  const songNumberList = Array.from({ length: 2000 }, (_, i) => i + 1).map(
    (num) => num.toString()
  );

  $: handleModifiedSearchTerm = (event: Event) => {
    searchTerm = (event as CustomEvent).detail;
  };

  $: filteredCards = songNumberList.filter((songNumberWhich) =>
    songNumberWhich.includes(searchTerm)
  );
</script>

<SearchBox on:searchTermModified={handleModifiedSearchTerm} />

<div class="card-grid-container">
  <div class="card-container">
    {#each filteredCards as filteredSongs}
      <a href="../hymnal/ag/{filteredSongs.padStart(4, '0')}.html">
        <h3
          class="song-number text-gray-300 bg-gray-50 hover:text-black hover:bg-white dark:text-gray-500  dark:bg-gray-700 dark:hover:text-white dark:hover:bg-gray-600 rounded-lg shadow-md transition duration-250 ease-in-out"
        >
          {filteredSongs}
        </h3>
      </a>
    {/each}
  </div>
</div>

<style>
  :root {
    --body-background: #222;
    --card-background: #333;
    --ring-offset-shadow: 0 0 #0000;
    --ring-shadow: 0 0 #0000;
    --text-color: #444;
  }
  .card-grid-container {
    @apply pt-8;
  }
  .card-container {
    display: grid;
    grid-gap: 1.5em;
    grid-template-columns: repeat(auto-fit, minmax(84px, 1fr));
  }

  .card-container > a {
    align-items: center;
    display: flex;
    justify-content: center;
    text-align: center;
    text-decoration: none;
  }

  .song-number {
    align-items: center;
    font-size: 2em;
    height: 100%;
    width: 100%;
  }

  .song-number:is(:hover, :focus-within) {
    background-position: 0;
    transform: scale(110%);
    transition: all 250ms ease-in-out;
  }
</style>
