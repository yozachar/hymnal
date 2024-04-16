<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let searchTerm = "";
  const dispatch = createEventDispatcher();

  $: handleInput = (event: Event) => {
    searchTerm = (event.target as HTMLInputElement).value;
    dispatch("searchTermModified", searchTerm);
  };
</script>

<div class="search-container">
  <div class="search-icon-container">
    <svg
      aria-hidden="true"
      class="search-icon"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      ><path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M24 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
      /></svg
    >
  </div>
  <input
    id="search-box"
    class="search-term"
    type="text"
    placeholder="Enter a song number ..."
    on:input={handleInput}
    bind:value={searchTerm}
  />
</div>

<style>
  .search-container {
    position: relative;
    width: 100%;
  }
  .search-icon-container {
    align-items: center;
    bottom: 0;
    display: flex;
    left: 0;
    padding-left: 0.75rem;
    pointer-events: none;
    position: absolute;
    top: 0;
  }
  .search-icon {
    color: #6b7280;
    /* height: 1.25rem; */
    width: 1.25rem;
  }
  .search-term {
    background-color: #374151;
    border-radius: 1.5rem;
    border: none;
    color: #ffffff;
    padding: 1rem 2.5rem;
    width: 100%;
  }
  .search-term:focus-within {
    border-width: 2px;
  }

  /* Light theme styles */
  @media (prefers-color-scheme: light) {
    .search-term {
      background-color: #f9fafb;
      color: #000000;
    }
  }
</style>
