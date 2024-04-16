<script lang="ts">
  import Landing from "./lib/Landing.svelte";
</script>

<main>
  <article>
    <h1
      class="heading pb-10 font-bold text-6xl text-center text-black dark:text-white"
    >
      ആത്മീയ ഗീതങ്ങൾ
    </h1>
    <Landing />
  </article>
  <footer>
    <h5 class="m-10">© Jovial Joe Jayarson</h5>
  </footer>
</main>

<style>
  .heading {
    font-family: NotoSerifMalayalam;
    font-size: clamp(8px, 8vw, 72px);
  }
  @media screen and (max-width: 768px) {
    .heading {
      width: 100%;
    }
  }
</style>
