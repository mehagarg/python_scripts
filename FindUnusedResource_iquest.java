import java.io.BufferedReader;
import java.io.File;
import java.io.FileFilter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Stack;

/**
 * Finds android resources which are not used. It needs to be run before release.
 * 
 * 
 */
public class FindUnusedResource {
  public static void main(String[] args) throws Exception {

    forAndroid();
    //forIphone();

  }

//  private static void forIphone() throws FileNotFoundException, IOException {
//    HashMap<String, String> resourcesForSearch = new HashMap<String, String>();
//
//    File resourcesFolder = new File(
//        "D://work//iQuest//Projects//TJ//Implementation//src//TripJournal//Resources//Images");
//    File[] files = null;
//    Stack<File> folders = new Stack<File>();
//    folders.add(resourcesFolder);
//    while (!folders.isEmpty()) {
//      resourcesFolder = folders.pop();
//
//      files = resourcesFolder.listFiles(new RegExpFileFilter(".*[\\.jpg|\\.png]"));
//      if (files != null) {
//        for (File file2 : files) {
//          String fileName = file2.getName();
//          if (fileName.contains(".")) {
//            fileName = fileName.substring(0, fileName.indexOf("."));
//          }
//          resourcesForSearch.put(fileName, file2.getAbsolutePath());
//        }
//
//      }
//
//      files = resourcesFolder.listFiles(new FolderFilter());
//      if (files != null) {
//        for (File file : files) {
//          folders.add(file);
//        }
//      }
//    }
//
//    System.out.println(resourcesForSearch.size() + "" + ": " + resourcesForSearch.keySet());
//
//    File targetFolder = new File("D://work//iQuest//Projects//TJ//Implementation//src//TripJournal//Classes");
//    folders = new Stack<File>();
//    folders.add(targetFolder);
//    while (!folders.isEmpty()) {
//      targetFolder = folders.pop();
//
//      files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.strings|\\.m|\\.mm|\\.cpp]"));
//      if (files != null) {
//        for (File file2 : files) {
//          checkFile(file2, resourcesForSearch);
//        }
//      }
//
//      files = targetFolder.listFiles(new FolderFilter());
//      if (files != null) {
//        for (File file : files) {
//          folders.add(file);
//        }
//      }
//
//    }
//
//    System.out.println("To be deleted after src: " + resourcesForSearch.size());
//    
//    
//    
//    targetFolder = new File("D://work//iQuest//Projects//TJ//Implementation//src//TripJournal");
//    folders = new Stack<File>();
//    folders.add(targetFolder);
//    while (!folders.isEmpty()) {
//      targetFolder = folders.pop();
//
//      files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.pbxproj]"));
//      if (files != null) {
//        for (File file2 : files) {
//          checkFile(file2, resourcesForSearch);
//        }
//      }
//
//      files = targetFolder.listFiles(new FolderFilter());
//      if (files != null) {
//        for (File file : files) {
//          folders.add(file);
//        }
//      }
//
//    }
//
//    System.out.println("To be deleted after project: " + resourcesForSearch.size());
//    
//
//    for (String filePath : resourcesForSearch.values()) {
//      File f = new File(filePath);
//      System.out.println("For deletion: " + f.getAbsolutePath());
//      // boolean success = f.delete();
//      // System.out.print(": " + success + "\n");
//    }
//  }

  private static void forAndroid() throws FileNotFoundException, IOException {
    HashMap<String, String> resourcesForSearch = new HashMap<String, String>();

    String rootDir = "/Users/meha/Documents/workspace/cloudon_091012/src/CloudOn";
    File resourcesFolder = new File(rootDir + "/res/drawable");
    File[] files = resourcesFolder.listFiles(new RegExpFileFilter(".*[\\.jpg|\\.png]"));
    for (File file : files) {
      String fileName = file.getName();
      fileName = fileName.substring(0, fileName.indexOf("."));
      resourcesForSearch.put(fileName, file.getAbsolutePath());
    }
    
    resourcesFolder = new File(rootDir + "/res/drawable-ldpi");
    files = resourcesFolder.listFiles(new RegExpFileFilter(".*[\\.jpg|\\.png]"));
    for (File file : files) {
      String fileName = file.getName();
      fileName = fileName.substring(0, fileName.indexOf("."));
      resourcesForSearch.put(fileName, file.getAbsolutePath());
    }
    
    resourcesFolder = new File(rootDir + "/res/drawable-mdpi");
    files = resourcesFolder.listFiles(new RegExpFileFilter(".*[\\.jpg|\\.png]"));
    for (File file : files) {
      String fileName = file.getName();
      fileName = fileName.substring(0, fileName.indexOf("."));
      resourcesForSearch.put(fileName, file.getAbsolutePath());
    }
    
    System.out.println(resourcesForSearch.size() + "" + ": " + resourcesForSearch.keySet());

    File targetFolder = new File(rootDir + "/res/values");
    files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.xml]"));
    for (File file : files) {
      checkFile(file, resourcesForSearch);
    }
    //System.out.println("To be deleted after values: " + resourcesForSearch.size());
    
    
    

    //System.out.println(resourcesForSearch.size() + "" + ": " + resourcesForSearch.keySet());

    targetFolder = new File(rootDir + "/res/layout");
    files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.xml]"));
    for (File file : files) {
      checkFile(file, resourcesForSearch);
    }
    //System.out.println("To be deleted after layouts: " + resourcesForSearch.size());
    
    targetFolder = new File(rootDir + "/res/drawable");
    files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.xml]"));
    for (File file : files) {
      checkFile(file, resourcesForSearch);
    }
    //System.out.println("To be deleted after drawables: " + resourcesForSearch.size());

    targetFolder = new File(rootDir + "/res/drawable-mdpi");
    files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.xml]"));
    for (File file : files) {
      checkFile(file, resourcesForSearch);
    }
    //System.out.println("To be deleted after drawables-mdpi: " + resourcesForSearch.size());

    targetFolder = new File(rootDir + "/res/drawable-ldpi");
    files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.xml]"));
    for (File file : files) {
      checkFile(file, resourcesForSearch);
    }
    //System.out.println("To be deleted after drawables-ldpi: " + resourcesForSearch.size());
    
    targetFolder = new File(rootDir + "/src");
    Stack<File> folders = new Stack<File>();
    folders.add(targetFolder);
    while (!folders.isEmpty()) {
      targetFolder = folders.pop();

      files = targetFolder.listFiles(new RegExpFileFilter(".*[\\.java]"));
      if (files != null) {
        for (File file2 : files) {
          checkFile(file2, resourcesForSearch);
        }
      }

      files = targetFolder.listFiles(new FolderFilter());
      if (files != null) {
        for (File file : files) {
          folders.add(file);
        }
      }

    }

    System.out.println("To be deleted after src: " + resourcesForSearch.size());

    for (String filePath : resourcesForSearch.values()) {
      File f = new File(filePath);
      System.out.print("File to delete: " + f.getAbsolutePath() + "\n");
      //boolean success = f.delete();
      //System.out.print(": " + success + "\n");
    }
  }

  private static void checkFile(File targetFile, HashMap<String, String> resourcesForSearch)
      throws FileNotFoundException, IOException {
    if (!targetFile.isFile()) {
      return;
    }
    BufferedReader r = new BufferedReader(new FileReader(targetFile));
    String readLine;
    StringBuilder sb = new StringBuilder();
    while ((readLine = r.readLine()) != null) {
      sb.append(readLine);
    }
    r.close();

    String bigOne = sb.toString();
    for (Iterator<Map.Entry<String, String>> it = resourcesForSearch.entrySet().iterator(); it.hasNext();) {
      Map.Entry<String, String> entry = it.next();
      if (bigOne.indexOf(entry.getKey()) >= 0) {
        System.out.println("Found: " + entry.getKey());
        it.remove();
      }
    }
  }

  private static class RegExpFileFilter implements FileFilter {
    private String regExp;

    public RegExpFileFilter(String regExp) {
      super();
      this.regExp = regExp;
    }

    @Override
    public boolean accept(File pathname) {
      return pathname.getName().matches(regExp);

    }

  }

  private static class FolderFilter implements FileFilter {

    @Override
    public boolean accept(File pathname) {
      return pathname.isDirectory() && !(".svn".equals(pathname.getName()));

    }

  }

}
