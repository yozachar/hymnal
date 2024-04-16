<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let searchTerm = "";
  const dispatch = createEventDispatcher();

  $: handleInput = (event: Event) => {
    searchTerm = (event.target as HTMLInputElement).value;
    dispatch("searchTermModified", searchTerm);
  };
</script>

<div class="search-container relative">
  <div
    class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
  >
    <svg
      aria-hidden="true"
      class="search-icon w-5 h-5 text-gray-500 dark:text-gray-400"
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
    class="search-term block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-3xl bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    type="text"
    placeholder="Enter a song number ..."
    on:input={handleInput}
    bind:value={searchTerm}
  />
</div>

<style>
  @media screen and (max-width: 768px) {
    .search-container {
      width: 100%;
    }
  }
</style>
