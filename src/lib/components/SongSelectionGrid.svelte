<script lang="ts">
  import SearchBox from "$lib/components/SearchBox.svelte";

  let searchTerm = "";

  const songNumberList = Array.from({ length: 1631 }, (_, i) => i + 1).map((num) => num.toString());

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
      <a href="/hymnal/ag/{filteredSongs.padStart(4, '0')}.html">
        <h3 class="song-number">{filteredSongs}</h3>
      </a>
    {/each}
  </div>
</div>

<style>
  .card-grid-container {
    padding: 2rem;
  }
  .card-container {
    display: grid;
    grid-gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(5.25rem, 1fr));
  }
  .card-container > a {
    text-decoration: none;
  }
  .song-number {
    align-items: center;
    background-color: #374151;
    border-radius: 0.5rem;
    color: #6b7280;
    font-size: 2em;
    height: 100%;
    padding: 0.5rem;
    transform: scale(100%);
    transition: 0.2s ease-in-out;
    width: 100%;
    box-shadow:
      0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
  .song-number:is(:hover, :focus-within) {
    background-color: #242424;
    box-shadow: none;
    color: #ffffff;
    transform: scale(110%);
    transition: 0.2s ease-in-out;
  }

  /* Dark theme styles */
  @media (prefers-color-scheme: light) {
    .song-number {
      background-color: #f9fafb;
      color: #d1d5db;
    }
    .song-number:is(:hover, :focus-within) {
      background-color: #ffffff;
      box-shadow: none;
      color: #000000;
    }
  }
</style>
