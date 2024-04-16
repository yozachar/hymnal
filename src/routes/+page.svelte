<script lang="ts">
  import SongSelectionGrid from "$lib/components/SongSelectionGrid.svelte";
  import "../../static/fonts/NotoSerifMalayalam/NotoSerifMalayalam.css";
  import "../../static/styles/global.css";
</script>

<svelte:head>
  <title>Multilingual Christian Hymnal</title>
</svelte:head>

<div class="app-container">
  <main>
    <h1 class="hymnal-name">ആത്മീയ ഗീതങ്ങൾ</h1>
    <p class="hymnal-description">
      പാട്ടുകളുടെ ക്രമം ആത്മീയ ഗീതങ്ങളുടെ 16-ാം പതിപ്പിൽ (ജനുവരി 2019),
      <span class="hymnal-publisher"> ജനറൽ YMEF </span>പ്രസിദ്ധീകരിച്ചതു പ്രകാരം
      <!-- The order of the songs are, as published in the 16th edition of Spiritual Hymns by General YMEF -->
    </p>
    <SongSelectionGrid />
  </main>
  <footer>
    <div class="copyleft-footer">
      All songs are owned by their respective authors<br />
      <a href="https://en.wikipedia.org/wiki/Copyleft"
        >Proprietary modifications to the source-code will NOT be allowed</a
      >
      |
      <a href="https://github.com/yozachar/hymnal/blob/main/LICENSE">🄯 Yozachar</a>
    </div>
  </footer>
</div>

<style>
  a {
    text-decoration: none;
  }
  footer {
    margin-top: auto;
  }

  .app-container {
    background-color: #242424;
    align-items: center;
    display: flex;
    flex-direction: column;
    min-height: 100svh;
    text-align: center;
  }
  .hymnal-description {
    color: gray;
    font-family: NotoSerifMalayalam;
    font-size: 1.5svw;
    padding: 1rem 2rem 3rem;
  }
  .hymnal-publisher {
    font-weight: bold;
  }
  .hymnal-name {
    color: #ffffff;
    font-family: NotoSerifMalayalam;
    font-size: 6svw;
    font-weight: 700;
    padding: 3rem 2rem 0.5rem;
  }
  .copyleft-footer,
  .copyleft-footer > a {
    color: gray;
    padding: 1rem;
  }
  .copyleft-footer > a:hover {
    color: cyan;
  }

  /* Light theme styles */
  @media (prefers-color-scheme: light) {
    a {
      color: #000000;
    }
    .app-container {
      background-color: #ffffff;
    }
    .hymnal-name {
      color: #000000;
    }
    .copyleft-footer > a:hover {
      color: darkcyan;
    }
  }
</style>
