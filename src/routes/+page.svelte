<script lang="ts">
  import SongSelectionGrid from "$lib/components/SongSelectionGrid.svelte";
  import "$lib/fonts/NotoSerifMalayalam/NotoSerifMalayalam.css";
  import "$lib/styles/global.css";
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
    <h5 class="copyleft-footer">
      All songs are owned by their respective authors<br />
      <a href="https://en.wikipedia.org/wiki/Copyleft"
        >Proprietary modifications to the source-code will NOT be allowed</a
      >
      |
      <a href="https://github.com/yozachar/hymnal/blob/main/LICENSE">🄯 Jovial Joe Jayarson</a>
    </h5>
  </footer>
</div>

<style>
  a {
    color: #ffffff;
    text-decoration: none;
  }
  a:hover {
    color: cyan;
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
    color: #ffffff;
    font-family: NotoSerifMalayalam;
    font-size: clamp(0.7rem, 1.7svw, 2rem);
    padding: 1rem 2rem 3rem;
  }
  .hymnal-publisher {
    font-weight: bold;
  }
  .hymnal-name {
    color: #ffffff;
    font-family: NotoSerifMalayalam;
    font-size: 3.5rem;
    font-size: clamp(2.5rem, 8svw, 10rem);
    font-weight: 700;
    padding-top: 3rem;
  }
  .copyleft-footer {
    color: #ffffff;
    padding: 1rem;
  }

  /* Light theme styles */
  @media (prefers-color-scheme: light) {
    a {
      color: #000000;
    }
    a:hover {
      color: darkcyan;
    }
    .app-container {
      background-color: #ffffff;
    }
    .hymnal-name {
      color: #000000;
    }
    .hymnal-description {
      color: #000000;
    }
    .copyleft-footer {
      color: #000000;
    }
  }
</style>
